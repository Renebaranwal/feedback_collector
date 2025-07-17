from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store feedback in memory
feedbacks = []

@app.route('/')
def index():
    return render_template('index.html', feedbacks=feedbacks)

@app.route('/add', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        feedbacks.append({'name': name, 'message': message})
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
