import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        print(f"\n📌 Columns in '{table_name}':")
        
        # Get column details for each table
        cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';")
        columns = cursor.fetchall()
        
        for col in columns:
            print(f"- {col[0]} ({col[1]})")

except Exception as e:
    print("❌ Error:", e)

finally:
    cursor.close()
    conn.close()
