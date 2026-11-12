# HomeTrack — Home Maintenance and Project Management System

## Project Overview

HomeTrack is a web-based information system developed for the Northwest Missouri State University MSIS Capstone Project.

The system is designed to help homeowners organize household maintenance tasks, manage home improvement projects, track expenses, and monitor maintenance schedules.

## Application Architecture

HomeTrack is a browser-based application using HTML, CSS, and Jinja templates for the frontend, Python and Flask for backend processing, and SQLite for relational data storage.

### Technology Stack

- Frontend (Implemented): HTML, CSS, and Jinja templates
- Frontend (Planned): JavaScript and Bootstrap
- Backend: Python and Flask
- Database: SQLite
- Version Control: Git and GitHub
- Development Environment: Visual Studio Code

## Primary User Roles

- Homeowner/Administrator: Manages household information, maintenance tasks, improvement projects, and expenses.
- Household Member: Views assigned maintenance tasks and updates their completion status.

## Main Use Cases

1. Create Maintenance Task
2. Complete Maintenance Task
3. Create Home Improvement Project
4. Record Project Expense

## Repository Organization

The HomeTrack repository is organized to separate frontend resources, backend application logic, database components, documentation, and testing.

- `templates/` — HTML templates for application pages and forms, including the maintenance task and home improvement project interfaces.
- `static/` — Folder reserved for CSS, JavaScript, and other frontend resources.
- `docs/` — Folder reserved for requirements, use cases, system diagrams, and supporting project documentation.
- `tests/` — Folder reserved for application testing and verification files.
- `app.py` — Main Flask application containing routes, form validation, backend logic, and database operations.
- `init_db.py` — Python script used to initialize the SQLite database.
- `schema.sql` — SQL definitions for the five database tables, including primary and foreign key relationships.
- `requirements.txt` — Python dependencies needed to install and run the application.
- `README.md` — Project overview, architecture, setup instructions, development progress, and known limitations.
- `.gitignore` — Excludes local environment files and the application database from version control.

The `hometrack.db` file stores application records locally and is excluded from GitHub. The repository contains the scripts needed to recreate the database structure.

The `static/` folder contains the custom CSS stylesheet used to style the HomeTrack interface. The `docs/` and `tests/` folders currently contain placeholder files and are reserved for future documentation and testing resources.

Git and GitHub are used to maintain version history, document development progress, and preserve working versions of the application throughout Modules 5, 6, and 7.

## Development Plan

### Module 5 — Initial Implementation
- Establish the application and database structure.
- Implement maintenance task creation.
- Implement home improvement project creation.
- Demonstrate initial working functionality.

### Module 6 – Continued Implementation
- Implemented maintenance task status updates (Not Started, In Progress, Completed).
- Implemented project expense recording with validation and SQLite storage.
- Added expense history and automatic project budget calculations.
- Integrated the new features with the existing HomeTrack interface.
- Verified task status persistence, expense recording, and spending calculations.

### Module 7 – Final Testing and Presentation
- Verified all four primary use cases through functional testing.
- Completed Python syntax checks and database schema verification.
- Confirmed SQLite database integrity and foreign key relationships.
- Tested data retrieval, project expense calculations, input validation, and error handling.
- Updated project documentation to reflect the completed prototype.
- Final presentation and submission are the remaining deliverables.

## Installation and Setup

HomeTrack is a web-based application developed using Python, Flask, HTML, CSS, and SQLite.

To set up the application:

1. Clone the GitHub repository to a local computer.
2. Open the project folder in Visual Studio Code.
3. Create and activate a Python virtual environment.
4. Install the dependencies listed in `requirements.txt`.
5. Run `python init_db.py` to create the SQLite database tables and automatically establish the demonstration household.
6. Run `python app.py` to start the Flask development server.
7. Open http://127.0.0.1:5000/ in a web browser.

The current prototype uses a local SQLite database and a predefined demonstration household with ID 1. The database is created automatically when the initialization script runs.

The `hometrack.db` file is excluded from GitHub through `.gitignore`. The repository includes the SQL schema and initialization script needed to recreate the database structure and demonstration household.

The application currently supports creating maintenance tasks and home improvement projects, saving records to SQLite, and displaying saved information.

## Current Project Status

HomeTrack is a functioning web-based prototype developed using Python, Flask, HTML, CSS, Jinja templates, and SQLite.

All four primary use cases have been implemented:

1. **Create Maintenance Task:** Users can create maintenance tasks with descriptions, priorities, and due dates.
2. **Update Maintenance Task Status:** Users can change task statuses between Not Started, In Progress, and Completed.
3. **Create Home Improvement Project:** Users can create projects with descriptions, estimated budgets, and target completion dates.
4. **Record Project Expenses:** Users can record expenses against existing projects and view expense history.

HomeTrack also automatically calculates total spending and remaining budgets for each home improvement project.

The application has been tested for task creation, project creation, status persistence, expense recording, and budget calculations involving multiple expenses. Development progress is maintained through GitHub.

## Known Limitations

HomeTrack is a functioning academic prototype that uses a predefined demonstration household rather than a complete user registration and authentication system. The application runs locally using Flask and SQLite and has not been deployed as a public website.

All four primary use cases have been implemented and functionally tested. Final verification included Python syntax checks, database schema initialization, SQLite integrity and foreign key checks, data retrieval, project budget calculations, input validation, and error handling.

Optional enhancements, including user authentication, advanced reporting, and notifications, remain outside the current implementation scope.
