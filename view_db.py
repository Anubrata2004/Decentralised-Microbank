from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Bank DB Viewer</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f5f5f5; padding: 30px; }
        h2 { color: #222; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 40px; }
        th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: left; }
        th { background: #eee; }
    </style>
</head>
<body>
    <h2>👤 Users</h2>
    <table>
        <tr><th>Name</th><th>Password</th><th>Sender Address</th><th>Assigned Bank Address</th><th>Private Key</th></tr>
        {% for u in users %}
            <tr>
                <td>{{ u[0] }}</td>
                <td>{{ u[1] }}</td>
                <td>{{ u[2] }}</td>
                <td>{{ u[3] }}</td>
                <td>{{ u[4] }}</td>
            </tr>
        {% endfor %}
    </table>

    <h2>👨‍💼 Admin</h2>
    <table>
        <tr><th>Name</th><th>Password</th><th>Address</th></tr>
        {% for a in admins %}
            <tr>
                <td>{{ a[0] }}</td>
                <td>{{ a[1] }}</td>
                <td>{{ a[2] }}</td>
            </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

@app.route('/')
def view_data():
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()

    cur.execute("SELECT name, password, sender_address, assigned_bank_address, private_key FROM users")

    users = cur.fetchall()

    cur.execute("SELECT name, password, address FROM admin")
    admin = cur.fetchall()

    conn.close()
    return render_template_string(TEMPLATE, users=users, admin=admin)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
