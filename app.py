from flask import Flask, render_template
from src.controller.HW_11controller import HW11_controller

app = Flask(__name__)

stevens_controller = HW11_controller("src/stevens_dir")


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/students")
def show_students():
    students = stevens_controller.list_students()
    return render_template("students.html", students=students)


@app.route("/instructor_courses")
def show_instructor_num():
    result, fields = stevens_controller.get_instructor_and_stu_num()
    return render_template("instructor_courses.html", item_list=result, fields=fields)


if __name__ == '__main__':
    app.run()
