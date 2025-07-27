from flask import Flask, render_template, request, redirect, url_for
from register_user import register_user
from register_admin import register_admin
from login_handler import login_user
from db import init_db
import os

app = Flask(__name__)

# Ensure DB is ready
if not os.path.exists('bank.db'):
    init_db()

@app.route('/')
def home():
    return '<h2>Welcome to Decentralized Banking</h2><p><a href="/register_user">Register as User</a> | <a href="/register_admin">Register as Admin</a> | <a href="/login">Login</a></p>'

# ---------- USER REGISTRATION ----------
@app.route('/register_user', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        sender_address = request.form['sender_address']
        private_key = request.form['private_key']
        assigned = register_user(name, password, sender_address, private_key)
        return f"<h3>Registration Successful!</h3><p>Your assigned bank account is:<br><b>{assigned}</b></p><a href='/'>Go Home</a>"
    return render_template('register_user.html')

# ---------- ADMIN REGISTRATION ----------
@app.route('/register_admin', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        result = register_admin(name, password)
        return f"<h3>{result}</h3><a href='/'>Go Home</a>"
    return render_template('register_admin.html')

# ---------- LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form['user_type']
        password = request.form['password']
        result = login_user(password, user_type)
        if result:
            if user_type == 'user':
                name, sender, assigned = result
                return f"<h3>Welcome {name}!</h3><p>Sender Address: {sender}<br>Assigned Bank Address: {assigned}</p><a href='/'>Home</a>"
            else:
                name, address = result
                return f"<h3>Welcome Admin {name}!</h3><p>Your MetaMask Address: {address}</p><a href='/'>Home</a>"
        else:
            return "<h3>Login failed. Invalid password or user type.</h3><a href='/login'>Try Again</a>"
    return render_template('login.html')

# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)
