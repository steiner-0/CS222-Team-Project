from database import *
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
# @app.route("/home")
# def home():
#     return "<h1>Home Page</h1>"


@app.route("/course")
def course():
    conn = create_course_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    courses = cur.fetchmany(10)
    
    return render_template('course.html', courses = courses)


if __name__ == '__main__':
    app.run(debug=True)