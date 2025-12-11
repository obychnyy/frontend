import sqlite3

DB_NAME = "modules.db"

def get_db():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS modules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        html TEXT,
        css TEXT
    );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
