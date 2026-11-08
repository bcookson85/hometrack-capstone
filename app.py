
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
            SELECT
                p.project_id,
                p.project_name,
                p.estimated_budget,
                p.target_completion_date,
                p.status,
                COALESCE(SUM(e.amount), 0) AS total_spent,
                p.estimated_budget - COALESCE(SUM(e.amount), 0) AS remaining_budget
            FROM home_improvement_projects AS p
            LEFT JOIN project_expenses AS e
                ON p.project_id = e.project_id
            WHERE p.household_id = ?
            GROUP BY p.project_id
            ORDER BY p.project_id DESC
            """,
            (DEMO_HOUSEHOLD_ID,),
        ).fetchall()
        
        expenses = connection.execute(
            """
            SELECT e.expense_id, p.project_name,
                   e.expense_description, e.amount, e.expense_date
            FROM project_expenses AS e
            JOIN home_improvement_projects AS p
                ON e.project_id = p.project_id
            WHERE p.household_id = ?
            ORDER BY e.expense_date DESC, e.expense_id DESC
            """,
            (DEMO_HOUSEHOLD_ID,),
        ).fetchall()
    
    return render_template(
        "index.html",
        tasks=tasks,
        projects=projects,
        expenses=expenses,
        error=error,
        created=request.args.get("created") == "1",
        project_created=request.args.get("project_created") == "1",
        expense_created=request.args.get("expense_created") == "1",
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

@app.route("/tasks/<int:task_id>/status", methods=["POST"])
def update_task_status(task_id):
    new_status = request.form.get("status", "").strip()

    if new_status not in ("Not Started", "In Progress", "Completed"):
        return "Please select a valid task status.", 400

    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        result = connection.execute(
            """
            UPDATE maintenance_tasks
            SET status = ?
            WHERE task_id = ? AND household_id = ?
            """,
            (new_status, task_id, DEMO_HOUSEHOLD_ID),
        )

        if result.rowcount == 0:
            return "Maintenance task not found.", 404

        connection.commit()

    return redirect(url_for("home"))


@app.route("/projects/expenses", methods=["POST"])
def record_project_expense():
    project_id_text = request.form.get("project_id", "").strip()
    description = request.form.get("expense_description", "").strip()
    amount_text = request.form.get("amount", "").strip()
    expense_date = request.form.get("expense_date", "").strip()

    if not project_id_text or not description or not amount_text or not expense_date:
        return "Please complete all required expense fields.", 400

    try:
        project_id = int(project_id_text)
        amount = float(amount_text)
        date.fromisoformat(expense_date)

        if project_id <= 0 or not isfinite(amount) or amount < 0:
            return "Please enter valid expense information.", 400
    except ValueError:
        return "Please enter a valid project, amount, and expense date.", 400

    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        project = connection.execute(
            """
            SELECT project_id
            FROM home_improvement_projects
            WHERE project_id = ? AND household_id = ?
            """,
            (project_id, DEMO_HOUSEHOLD_ID),
        ).fetchone()

        if project is None:
            return "Home improvement project not found.", 404

        connection.execute(
            """
            INSERT INTO project_expenses
                (project_id, expense_description, amount, expense_date)
            VALUES (?, ?, ?, ?)
            """,
            (project_id, description, amount, expense_date),
        )
        
        connection.execute(
            """
            UPDATE home_improvement_projects
            SET status = 'In Progress'
            WHERE project_id = ?
              AND household_id = ?
              AND status = 'Not Started'
            """,
            (project_id, DEMO_HOUSEHOLD_ID),
        )

        connection.commit()

    return redirect(url_for("home", expense_created="1"))

if __name__ == "__main__":
    app.run(debug=True)
