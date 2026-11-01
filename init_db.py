
import sqlite3
from pathlib import Path

# Locate the database and schema files
project_folder = Path(__file__).parent
database_path = project_folder / "hometrack.db"
schema_path = project_folder / "schema.sql"

# Connect to SQLite and create the database tables
connection = sqlite3.connect(database_path)
connection.execute("PRAGMA foreign_keys = ON")

with open(schema_path, "r", encoding="utf-8") as schema_file:
    connection.executescript(schema_file.read())

# Create the demonstration household if it does not exist
connection.execute(
    """
    INSERT OR IGNORE INTO households
    (household_id, household_name, property_address)
    VALUES (1, 'Demo Household', '123 Example Lane')
    """
)

connection.commit()

connection.close()

print("HomeTrack database initialized successfully!")
