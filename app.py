from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# DB initialization (run only once)
def init_db():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedbacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Home route
@app.route('/')
def index():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, message FROM feedbacks")
    feedbacks = cursor.fetchall()
    conn.close()
    return render_template('index.html', feedbacks=feedbacks)

# Add feedback
@app.route('/add', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedbacks (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5001)  
