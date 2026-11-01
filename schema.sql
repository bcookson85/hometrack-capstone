CREATE TABLE IF NOT EXISTS households (
    household_id INTEGER PRIMARY KEY AUTOINCREMENT,
    household_name TEXT NOT NULL,
    property_address TEXT,
    administrator_user_id INTEGER,
    FOREIGN KEY (administrator_user_id)
        REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    household_id INTEGER,
    name TEXT NOT NULL,
    email_address TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    account_status TEXT DEFAULT 'Active',
    household_role TEXT NOT NULL,
    FOREIGN KEY (household_id)
        REFERENCES households(household_id)
);

CREATE TABLE IF NOT EXISTS maintenance_tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    household_id INTEGER NOT NULL,
    assigned_user_id INTEGER,
    task_name TEXT NOT NULL,
    description TEXT,
    priority TEXT NOT NULL,
    due_date TEXT NOT NULL,
    recurrence_interval INTEGER,
    status TEXT NOT NULL DEFAULT 'Not Started',
    completion_date TEXT,
    FOREIGN KEY (household_id)
        REFERENCES households(household_id),
    FOREIGN KEY (assigned_user_id)
        REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS home_improvement_projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    household_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT,
    estimated_budget REAL NOT NULL,
    target_completion_date TEXT,
    status TEXT NOT NULL DEFAULT 'Not Started',
    FOREIGN KEY (household_id)
        REFERENCES households(household_id)
);

CREATE TABLE IF NOT EXISTS project_expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    expense_description TEXT NOT NULL,
    amount REAL NOT NULL,
    expense_date TEXT NOT NULL,
    FOREIGN KEY (project_id)
        REFERENCES home_improvement_projects(project_id)
);
