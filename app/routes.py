from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, User, Formulir

# Create Blueprint instead of Flask app instance
routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return redirect(url_for('routes.login'))

@routes.route('/register', methods=['GET', 'POST'])
def register():
    # Redirect if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('routes.main'))

    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            
            if not username or not password:
                flash('Username and password are required', 'error')
                return redirect(url_for('routes.register'))

            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                flash('Username already exists', 'error')
                return redirect(url_for('routes.register'))
            
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful', 'success')
            return redirect(url_for('routes.login'))
            
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')
            return redirect(url_for('routes.register'))

    return render_template('register.html')

@routes.route('/login', methods=['GET', 'POST']) 
def login():
    # Redirect if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('routes.main'))

    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            
            if not username or not password:
                flash('Username and password are required', 'error')
                return redirect(url_for('routes.login'))

            user = User.query.filter_by(username=username).first()
            
            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for('routes.main'))
                
            flash('Invalid username or password', 'error')
            
        except Exception as e:
            flash('Login failed. Please try again.', 'error')
            
    return render_template('login.html')

@routes.route('/main')
@login_required
def main():
    return render_template('main.html')

@routes.route('/formulir', methods=['GET'])
@login_required
def formulir():
    # Check if user already has a form
    if current_user.formulir:
        flash('You have already submitted a form', 'warning')
        return redirect(url_for('routes.main'))
    return render_template('formulir.html')

@routes.route('/view-formulir')
@login_required
def view_formulir():
    if not current_user.formulir:
        flash('You have not submitted any form yet', 'warning')
        return redirect(url_for('routes.main'))
    return render_template('view_formulir.html')

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('routes.login'))