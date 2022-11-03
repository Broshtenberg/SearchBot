import sqlite3 as sql

base = sql.connect("targetapp.db")
cur = base.cursor()

# Create table fot new users
with base:
    base.execute("CREATE TABLE IF NOT EXISTS users(user_id, user_name, service, status, date)")


# checked user in database
def check_user(message):
    with base:
        user = cur.execute("SELECT * FROM users WHERE user_id = ?", (message.from_user.id,)).fetchall()
    return bool(len(user))


# added user to database
def add_user(service, message):
    with base:
        base.execute("INSERT INTO users(user_id, user_name, service, status, date) VALUES(?, ?, ?, ?, ?)",
                     (message.from_user.id, message.from_user.username, service, "free", message.date))
