from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('profile'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        birthday = request.form.get('birthday')

        if not all([username, email, password, full_name, birthday]):
            return render_template('register.html', error='সব field fill করুন!')

        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='এই username ইতিমধ্যে আছে!')

        if User.query.filter_by(email=email).first():
            return render_template('register.html', error='এই email ইতিমধ্যে আছে!')

        try:
            birthday_date = datetime.strptime(birthday, '%Y-%m-%d').date()
            user = User(
                username=username,
                email=email,
                full_name=full_name,
                birthday=birthday_date
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            return render_template('register.html', error=f'Error: {str(e)}')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('profile'))
        else:
            return render_template('login.html', error='Username বা password ভুল!')

    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if not user:
        return redirect(url_for('login'))

    # Birthday calculation
    today = datetime.now().date()
    birthday = user.birthday
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    # Check if birthday is today
    is_birthday_today = (today.month == birthday.month and today.day == birthday.day)

    return render_template('profile.html', user=user, age=age, is_birthday_today=is_birthday_today)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)