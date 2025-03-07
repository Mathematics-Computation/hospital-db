import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()

    print("\n📌 Existing Tables:")
    for table in tables:
        print(f"- {table[0]}")

except Exception as e:
    print("❌ Error:", e)

finally:
    cursor.close()
    conn.close()
