import sqlite3
import pandas as pd
def create_course_db_conn():
    conn = sqlite3.connect('course.db')
    return conn

def get_feedback():
    print("Nice!")
