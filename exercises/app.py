from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)
# @app.route('/')
# def home1 () :
#     return render_template(
#         'student.html')
    
@app.route('/')
def home():
    return render_template(
        'home.html')

@app.route('/student/<int:student_id>')
def display_student(student_id):
    student= session.query(student_id
    ).first()
    return render_template(
        'student.html', n = student_id)        

app.run(debug=True)
