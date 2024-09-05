import sqlite3

def create_db():
    conn = sqlite3.connect("mulla")  # Database named "mulla"
    cursor = conn.cursor()

    # Table for tracking groups
    cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id INTEGER NOT NULL UNIQUE)''')

    # Table for tracking users
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL UNIQUE)''')

    conn.commit()
    conn.close()

def add_group(group_id):
    conn = sqlite3.connect("mulla")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO groups (group_id) VALUES (?)", (group_id,))
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect("mulla")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect("mulla")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM groups")
    total_groups = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    conn.close()
    return total_groups, total_users
