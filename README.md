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

The `static/`, `docs/`, and `tests/` folders currently contain placeholder files and will be populated as development continues.

Git and GitHub are used to maintain version history, document development progress, and preserve working versions of the application throughout Modules 5, 6, and 7.

## Development Plan

### Module 5 — Initial Implementation
- Establish the application and database structure.
- Implement maintenance task creation.
- Implement home improvement project creation.
- Demonstrate initial working functionality.

### Module 6 — Continued Implementation
- Implement maintenance task completion.
- Implement project expense recording and budget calculations.
- Integrate and test the major application functions.

### Module 7 — Final Testing and Presentation
- Verify the primary use cases.
- Address remaining errors and incomplete functionality.
- Update documentation and demonstrate the final prototype.

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

The HomeTrack development environment, Flask application, and SQLite database have been established. Two primary use cases have been implemented and successfully tested: Create Maintenance Task and Create Home Improvement Project. Both functions allow users to enter information, save records to SQLite, and retrieve the saved information for display. Additional functionality, including task completion and project expense tracking, will be developed during Module 6.

## Known Limitations

HomeTrack is currently a working prototype with maintenance task creation and home improvement project creation implemented. The application uses a predefined demonstration household rather than a complete user authentication system. Maintenance task completion, project expense tracking, budget calculations, and additional reporting features have not yet been implemented. These functions will be addressed during subsequent development modules.

## Academic Purpose

This repository contains coursework developed for the MSIS Capstone Project at Northwest Missouri State University. Development will use fictional demonstration data, and sensitive credentials will not be committed.
