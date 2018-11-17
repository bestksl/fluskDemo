# @Author: HaoxuanLi  
# @Date 2018/11/11
# CWID: 10434197
from src.DAO.dao import Dao
from src.Domain.Student import Student
from src.Utils.FileReader import FileReader


class StudentService:
    def __init__(self):
        self.dao = Dao.get_instance()
        self.table_exist = False

    def save_student(self, student: Student):
        if not self.dao.if_exist("student"):
            raise Exception(f"Error: student table not exist")
        sql = '''insert into student values (?,?,?)'''
        args = (student.cwid, student.name, student.major_name)
        self.dao.execute_sql(sql, args)

    def create_student_table(self, header: tuple):
        self.dao.create_table("student", header)

    def find_student(self, cwid: str):
        sql = '''select CWID, Name, Major from student where student.CWID=?'''
        arg = (cwid,)
        result_tuple = self.dao.execute_sql(sql, arg)[0]
        result_stu = Student(result_tuple[0], result_tuple[1], result_tuple[2])
        return result_stu

    def get_stu_num(self):
        if not self.dao.if_exist("student"):
            sql = ''
            return

    def read_student_from_file(self, path: str):
        if self.dao.if_exist("student"):
            return
        lines = FileReader.read_lines(path)
        header = [attr + " varchar(50)" for attr in lines[0]]
        header[0] += " PRIMARY KEY"
        self.create_student_table(tuple(header))
        for attr in lines[1:len(lines)]:
            stu = Student(attr[0], attr[1], attr[2])
            self.save_student(stu)

    def num_of_stu_by_major(self):
        sql = '''select Major, count(*) from student group by student.Major'''
        result = self.dao.execute_sql(sql)
        return result

    def get_all_student(self):
        stu_list = []
        sql = '''select CWID, Name, Major from student'''
        result_list = self.dao.execute_sql(sql)
        for result_tuple in result_list:
            stu_list.append(Student(result_tuple[0], result_tuple[1], result_tuple[2]))
        return stu_list