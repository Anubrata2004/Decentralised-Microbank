import sqlite3

def init_db():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 name TEXT,
                 password TEXT,
                 sender_address TEXT,
                 private_key TEXT,
                 assigned_bank_address TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS admin (
                 name TEXT,
                 password TEXT,
                 address TEXT)''')
    conn.commit()
    conn.close()
