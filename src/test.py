# @Author: HaoxuanLi
# @Date 2018/11/4
# CWID: 10434197
import unittest

from src.DAO.dao import Dao
from src.Service.grade_services import GradeService
from src.Service.instructor_services import InstructorService
from src.Service.major_services import MajorService
from src.Service.student_services import StudentService
from src.controller.HW_11controller import HW11_controller


class MyTest(unittest.TestCase):
    dao = Dao.get_instance()
    sc = StudentService()
    i_s = InstructorService()
    gs = GradeService()
    ms = MajorService()
    controller = HW11_controller("stevens_dir")

    # def test_dao(self):
    #     self.dao.execute_sql("create table test (id,name)")
    #
    # def test_insert(self):
    #     self.dao.execute_sql('''insert into test values (?,?)''', ('149', 'will'))
    #
    # def test_query(self):
    #     print(self.dao.execute_sql('''select * from test where name=?''', ('ksl',)))
    #
    # def test_student_services(self):
    #     header = ("CWID varchar(50)", "name varchar(50)", "major varchar(50)")
    #     self.sc.create_student_table(header)
    #     stu = Student("15555", "kslksl", "software engineering")
    #     self.sc.save_student(stu)
    #     stu_new = self.sc.find_student("15555")
    #     print(stu_new.cwid, stu_new.name, stu_new.major_name)
    #
    # def test_instructor_services(self):
    #     header = ("CWID varchar(50)", "NAME varchar(50)", "DEPT varchar(50)")
    #     self.i_s.create_instructor_table(header)
    #     ins = Instructor("777555", "instrucname", "se")
    #     self.i_s.save_instructor(ins)
    #     new_ins = self.i_s.find_instructor("777555")
    #     print(new_ins.cwid, new_ins.name, new_ins.dept)
    #
    # def test_grade_services(self):
    #     header = ("Student_CWID varchar(50)", "Course varchar(50)", "Grade varchar(50)", "Instructor_CWID varchar(50)")
    #     self.gs.create_grade_table(header)
    #     grade = Grade("1111", "ssw 810", "A+", "555")
    #     self.gs.save_grade(grade)
    #     result_grade = self.gs.find_grade("1111", "ssw 810")
    #     print(result_grade.stu_id, result_grade.course_name, result_grade.score, result_grade.ins_id)
    #
    # def test_major_services(self):
    #     header = ("Major varchar(50)", "Course varchar(50)")
    #     self.ms.create_major_table(header)
    #     self.ms.save_major("se", "ssw 564")
    #     self.ms.save_major("se", "ssw 567")
    #     self.ms.save_major("se", "ssw 810")
    #     self.ms.save_major("fe", "fe 577")
    #     self.ms.save_major("cs", "cs 568")
    #     result_course = self.ms.find_courses("se")
    #     print(result_course)

    def test_HW11controller(self):
        self.controller.answers()
