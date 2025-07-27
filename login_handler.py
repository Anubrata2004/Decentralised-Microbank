import sqlite3

def login_user(password, user_type):
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    if user_type.lower() == "user":
        c.execute("SELECT name, sender_address, assigned_bank_address FROM users WHERE password=?", (password,))
        result = c.fetchone()
    elif user_type.lower() == "admin":
        c.execute("SELECT name, address FROM admin WHERE password=?", (password,))
        result = c.fetchone()
    else:
        result = None
    conn.close()
    return result
