from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import Student

app = Flask(__name__)
# db = SQLAlchemy(app)  --this will only when you dont have any orm(class)
app.config.from_pyfile('config.py')
db.init_app(app)
@app.route('/')
def home():
    return 'homepage'

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        rollno = request.form['rollno']
        name = request.form['name']
        course = request.form['course']
        new_record = Student(RollNo = rollno,Name=name,Course=course)
        db.session.add(new_record)
        db.session.commit()
        flash("record inserted into database")
        return redirect(url_for('login'))
    return render_template("base.html")

@app.route('/dbcreate')
def dbcreate():
    db.create_all()
    return 'Database created sucessfully'




if __name__=='__main__':
    app.run(debug=True)
