import json
import random
import sqlite3
from db import init_db

def register_user(name, password, sender_address, private_key):
    with open('ganache_accounts.json', 'r') as f:
        data = json.load(f)
        for acc in data['empty']:
            if not acc['assigned']:
                assigned_address = acc['address']
                acc['assigned'] = True
                break
        else:
            return "No empty account available."

    with open('ganache_accounts.json', 'w') as f:
        json.dump(data, f, indent=4)

    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)",
              (name, password, sender_address, private_key, assigned_address))
    conn.commit()
    conn.close()

    return assigned_address
