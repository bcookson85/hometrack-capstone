
import sqlite3
from contextlib import closing
from datetime import date
from pathlib import Path

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

    return render_template(
        "index.html",
        tasks=tasks,
        error=error,
        created=request.args.get("created") == "1",
    )


if __name__ == "__main__":
    app.run(debug=True)
