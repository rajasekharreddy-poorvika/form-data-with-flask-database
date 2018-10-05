from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Student(db.Model):
    RollNo = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(10))
    Course = db.Column(db.String(10))
