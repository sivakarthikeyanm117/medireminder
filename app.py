from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

APP_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(APP_DIR, 'users.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL)'
    )
    conn.commit()
    conn.close()

app = Flask(__name__)
app.secret_key = os.environ.get('MEDISECRET', 'dev-secret-change-me')

# Initialize the database on import to ensure the users table exists.
init_db()

def get_user_by_username(username):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT id, username, password_hash FROM users WHERE username = ?', (username,))
    row = cur.fetchone()
    conn.close()
    return row

def create_user(username, password):
    password_hash = generate_password_hash(password)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        return True, None
    except sqlite3.IntegrityError as e:
        return False, str(e)
    finally:
        conn.close()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        if not username or not password:
            flash('Please enter both username and password', 'warning')
            return redirect(url_for('login'))

        user = get_user_by_username(username)
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Logged in successfully', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        password2 = request.form.get('password2', '')

        if not username or not password:
            flash('Please provide username and password', 'warning')
            return redirect(url_for('register'))
        if password != password2:
            flash('Passwords do not match', 'warning')
            return redirect(url_for('register'))

        ok, err = create_user(username, password)
        if ok:
            flash('Registration successful. Please login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Registration failed: ' + (err or 'unknown'), 'danger')
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('login'))
    username = session.get('username')
    return render_template('dashboard.html', username=username)

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Run in debug mode for local testing. In production, use a WSGI server.
    app.run(host='127.0.0.1', port=5000, debug=True)
