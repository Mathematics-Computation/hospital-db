# Hospital Database Showcase

This project demonstrates a PostgreSQL-based hospital database system with schema creation, updates, and querying using Python.

## Project Files

### 1. `schema.sql`
- Defines the initial database schema.
- Creates three tables: `patients`, `doctors`, and `appointments`.
- Establishes relationships between tables.

### 2. `update.sql`
- Adds new features and improvements.
- Creates the `patient_diseases` table.
- Adds `address` column to `patients`.
- Adds `hospital_affiliation` column to `doctors`.
- Indexes `disease_id` for performance.
- Creates a trigger to auto-update `recovery_date`.

### 3. `connect.py`
- Establishes a connection to the PostgreSQL database.
- Loads environment variables from `.env`.

### 4. `update.py`
- Checks if updates have already been applied.
- Executes `update.sql` only if needed.
- Displays the updated schema.

### 5. `check_tables.py`
- Lists all tables in the database.
- Useful for verifying the schema.

### 6. `check_columns.py`
- Prints all columns for each table.
- Useful for debugging and schema validation.

### 7. `update2.sql`
This SQL file updates the `hospital-db` by adding Role-Based Access Control (RBAC) tables: `roles` and `users`. These tables help manage access levels within the system.


### 8. `update2.py`
This Python script connects to the Postgres database and applies `update2.sql`, ensuring that the new `roles` and `users` tables are created.

#### Script Workflow:
- Connects to the PostgreSQL database using credentials from `.env`
- Reads `update2.sql` and executes the SQL commands
- Confirms the successful execution





## Running the Project
1. Ensure PostgreSQL is running and accessible.
2. Create and configure the `.env` file with `DATABASE_URL`.
3. Execute the scripts as needed:
   ```sh
   python connect.py  # Check database connection
   python update.py   # Apply updates if needed
   python check_tables.py  # List all tables
   python check_columns.py # Show table columns
   ```

## Learning Outcomes
- Writing and updating SQL schemas.
- Using Python (`psycopg2`) to interact with PostgreSQL.
- Automating schema management with scripts.
- Showcasing incremental database updates professionally.

