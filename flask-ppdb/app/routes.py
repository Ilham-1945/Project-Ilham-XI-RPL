from flask import render_template, request, redirect, url_for
from .models import Student
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        # Add logic to save the student data to the database
        new_student = Student(name=name, age=age)
        new_student.save()  # Assuming a save method exists in the Student model
        return redirect(url_for('index'))
    return render_template('form.html')