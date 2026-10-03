import sqlite3

conn = sqlite3.connect(
    "smartvote.db",
    check_same_thread=False
)

cursor = conn.cursor()

# USERS TABLE
cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    age INTEGER,

    voter_id TEXT UNIQUE,

    phone TEXT UNIQUE,

    aadhaar TEXT UNIQUE,

    password TEXT,

    has_voted INTEGER DEFAULT 0
)

""")

# VOTES TABLE
cursor.execute("""

CREATE TABLE IF NOT EXISTS votes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    voter_id TEXT UNIQUE,

    candidate TEXT
)

""")

conn.commit()