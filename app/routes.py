from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, User, Formulir

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return redirect(url_for('routes.login'))

@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = (request.form['password'])
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('user.dashboard') if user.role == 'user' else url_for('admin.dashboard'))
        ("Login gagal")
    return render_template('login.html')
