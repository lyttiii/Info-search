from app import db
from flask_login import UserMixin
from datetime import date

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(200))

    def __repr__(self):
        return f'<User {self.username}>'


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    short_name = db.Column(db.String(50), nullable=False)
    creation_date = db.Column(db.Date, nullable=False)
    
    students = db.relationship('Student', backref='university', lazy=True)
    
    def __repr__(self):
        return f'<University {self.short_name}>'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    enrollment_year = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Student {self.full_name}>'

