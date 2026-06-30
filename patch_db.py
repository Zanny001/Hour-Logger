import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DB_URL)
cursor = conn.cursor()

try:
    # Safely add the missing column to your live production database
    cursor.execute("ALTER TABLE sessions ADD COLUMN IF NOT EXISTS session_date TEXT DEFAULT '';")
    conn.commit()
    print("Success: 'session_date' column added perfectly!")
except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
