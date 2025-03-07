import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # Load environment variables from .env

DATABASE_URL = os.getenv("DATABASE_URL")  # Get DB URL from .env

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Read and execute schema.sql
with open("schema.sql", "r") as file:
    sql_commands = file.read()
    cursor.execute(sql_commands)  # Executes SQL script

conn.commit()  # Commit changes
print(" Tables created successfully in Neon!")

# Close connection
cursor.close()
conn.close()