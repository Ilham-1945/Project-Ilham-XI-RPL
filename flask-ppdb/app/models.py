from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Student {self.name}>'