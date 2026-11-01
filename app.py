
import sqlite3
from contextlib import closing
from datetime import date
from pathlib import Path
from math import isfinite

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

DATABASE_PATH = Path(__file__).with_name("hometrack.db")
DEMO_HOUSEHOLD_ID = 1


@app.route("/", methods=["GET", "POST"])
def home():
    error = None

    if request.method == "POST":
        task_name = request.form.get("task_name", "").strip()
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "").strip()
        due_date = request.form.get("due_date", "").strip()

        if not task_name or not priority or not due_date:
            error = "Please complete all required fields."
        elif priority not in ("Low", "Medium", "High"):
            error = "Please select a valid priority."
        else:
            try:
                date.fromisoformat(due_date)
            except ValueError:
                error = "Please enter a valid due date."

        if error is None:
            with closing(sqlite3.connect(DATABASE_PATH)) as connection:
                connection.execute("PRAGMA foreign_keys = ON")
                connection.execute(
                    """
                    INSERT INTO maintenance_tasks
                    (household_id, task_name, description, priority, due_date)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        DEMO_HOUSEHOLD_ID,
                        task_name,
                        description,
                        priority,
                        due_date,
                    ),
                )
                connection.commit()

            return redirect(url_for("home", created="1"))

    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        connection.row_factory = sqlite3.Row
        tasks = connection.execute(
            """
            SELECT task_id, task_name, priority, due_date, status
            FROM maintenance_tasks
            WHERE household_id = ?
            ORDER BY due_date, task_id
            """,
            (DEMO_HOUSEHOLD_ID,),
        ).fetchall()
        
        projects = connection.execute(
            """
            SELECT project_id, project_name, estimated_budget,
                   target_completion_date, status
            FROM home_improvement_projects
            WHERE household_id = ?
            ORDER BY project_id DESC
            """,
            (DEMO_HOUSEHOLD_ID,),
        ).fetchall()

    
    return render_template(
        "index.html",
        tasks=tasks,
        projects=projects,
        error=error,
        created=request.args.get("created") == "1",
        project_created=request.args.get("project_created") == "1",
    )


@app.route("/projects", methods=["POST"])
def create_project():
    project_name = request.form.get("project_name", "").strip()
    description = request.form.get("description", "").strip()
    budget_text = request.form.get("estimated_budget", "").strip()
    target_date = request.form.get("target_completion_date", "").strip()

    if not project_name or not budget_text or not target_date:
        return "Please complete all required project fields.", 400

    try:
        estimated_budget = float(budget_text)
        date.fromisoformat(target_date)

        if not isfinite(estimated_budget) or estimated_budget < 0:
            return "Please enter a valid project budget.", 400

    except ValueError:
        return "Please enter a valid budget and completion date.", 400

    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(
            """
            INSERT INTO home_improvement_projects
            (household_id, project_name, description,
             estimated_budget, target_completion_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                DEMO_HOUSEHOLD_ID,
                project_name,
                description,
                estimated_budget,
                target_date,
            ),
        )
        connection.commit()

    return redirect(url_for("home", project_created="1"))

if __name__ == "__main__":
    app.run(debug=True)
