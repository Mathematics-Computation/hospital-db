import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    print("🔍 Checking for updates...")

    # Check if columns exist before adding
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'patients' AND column_name = 'address';")
    address_exists = cursor.fetchone()

    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'doctors' AND column_name = 'hospital_affiliation';")
    hospital_affiliation_exists = cursor.fetchone()

    if address_exists and hospital_affiliation_exists:
        print("✅ Updates already applied. No changes needed.")
    else:
        print("🚀 Applying updates...")
        with open("update.sql", "r") as f:
            cursor.execute(f.read())
        conn.commit()
        print("✅ Database updated successfully!")

    # Show updated schema for verification
    cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'patients';")
    print("\n📌 Updated 'patients' schema:")
    for row in cursor.fetchall():
        print(f"- {row[0]} ({row[1]})")

    cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'doctors';")
    print("\n📌 Updated 'doctors' schema:")
    for row in cursor.fetchall():
        print(f"- {row[0]} ({row[1]})")

except Exception as e:
    print("❌ Error:", e)

finally:
    cursor.close()
    conn.close()
