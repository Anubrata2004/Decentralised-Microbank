import sqlite3
from db import init_db

def register_admin(name, password):
    address = "0x92b2422E8597482C106Be235d6c3B06CEc270184"
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute("INSERT INTO admin VALUES (?, ?, ?)", (name, password, address))
    conn.commit()
    conn.close()
    return "Admin registered successfully."
