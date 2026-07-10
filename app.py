from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'task-management-super-secret-key-vercel'

# Hardcoded admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password123'

DATABASE = '/tmp/task_management.db' if os.environ.get('VERCEL') else 'task_management.db'

@app.before_request
def ensure_db():
    if os.environ.get('VERCEL'):
        if not os.path.exists(DATABASE):
            from database import init_db
            init_db()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('dashboard'))

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid credentials. Please try again.'

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    db = get_db()
    
    if request.method == 'POST':
        # Handle task assignment
        employee_name = request.form['employee_name']
        task_title_id = request.form['task_title_id']
        
        if employee_name and task_title_id:
            db.execute('INSERT INTO Task_Management (employee_name, task_title_id) VALUES (?, ?)',
                       (employee_name, task_title_id))
            db.commit()
            return redirect(url_for('dashboard'))

    # Fetch task titles for dropdown
    cur = db.execute('SELECT id, title FROM Task_Titles')
    task_titles = cur.fetchall()

    # Fetch tasks assigned
    cur = db.execute('''
        SELECT tm.id, tm.employee_name, tt.title as task_title, tm.completed
        FROM Task_Management tm
        JOIN Task_Titles tt ON tm.task_title_id = tt.id
        ORDER BY tm.id DESC
    ''')
    tasks = cur.fetchall()

    return render_template('dashboard.html', task_titles=task_titles, tasks=tasks)

@app.route('/toggle_task/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
        
    db = get_db()
    
    # Get current status
    cur = db.execute('SELECT completed FROM Task_Management WHERE id = ?', (task_id,))
    task = cur.fetchone()
    
    if task:
        new_status = 1 if task['completed'] == 0 else 0
        db.execute('UPDATE Task_Management SET completed = ? WHERE id = ?', (new_status, task_id))
        db.commit()
        
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    from database import init_db
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)
