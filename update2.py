import psycopg2
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to DB
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Read SQL file
with open("update2.sql", "r") as f:
    sql_script = f.read()

# Execute SQL
cur.execute(sql_script)

# Commit & close
conn.commit()
cur.close()
conn.close()

print("Database updated successfully!")
