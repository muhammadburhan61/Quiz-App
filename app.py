from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user and quiz data
users = {'test@example.com': 'password123'}
quiz_questions =  [
    {
        "question": "What does HTML stand for?",
        "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language", "Hyper Tool Multi Language"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which HTML tag is used to insert an image?",
        "options": ["<img>", "<image>", "<pic>", "<src>"],
        "answer": "<img>"
    },
    {
        "question": "Which property is used to change the background color in CSS?",
        "options": ["color", "bgcolor", "background-color", "background"],
        "answer": "background-color"
    },
    {
        "question": "What does the CSS 'position: absolute;' do?",
        "options": ["Fixes the element to the top", "Positions the element based on browser window", "Removes the element", "Positions relative to the nearest positioned ancestor"],
        "answer": "Positions relative to the nearest positioned ancestor"
    },
    {
        "question": "Which keyword is used to declare a variable in JavaScript?",
        "options": ["let", "var", "const", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Which built-in method is used to remove the last element from an array in JavaScript?",
        "options": ["pop()", "shift()", "remove()", "delete()"],
        "answer": "pop()"
    },
    {
        "question": "Which of the following is a correct way to create a function in JavaScript?",
        "options": ["function myFunc()", "func myFunc()", "create function myFunc()", "new function myFunc()"],
        "answer": "function myFunc()"
    },
    {
        "question": "What is the correct syntax to define a function in Python?",
        "options": ["def myFunc():", "function myFunc():", "create myFunc():", "func myFunc()"],
        "answer": "def myFunc():"
    },
    {
        "question": "Which of these is a Python list?",
        "options": ["{1, 2, 3}", "[1, 2, 3]", "(1, 2, 3)", "<1, 2, 3>"],
        "answer": "[1, 2, 3]"
    },
    {
        "question": "Which statement is used to handle exceptions in Python?",
        "options": ["try/except", "do/catch", "try/catch", "handle/error"],
        "answer": "try/except"
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            session['user'] = email
            return redirect(url_for('quiz'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users:
            return render_template('register.html', error="Email already registered")
        users[email] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'user' not in session:
        return redirect(url_for('login'))
    user = session['user']  # get logged-in user email
    if request.method == 'POST':
        score = 0
        for i, q in enumerate(quiz_questions):
            if request.form.get(f'q{i}') == q['answer']:
                score += 1
        return render_template('result.html', score=score, total=len(quiz_questions), user=user)
    return render_template('quiz.html', questions=quiz_questions, user=user)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
