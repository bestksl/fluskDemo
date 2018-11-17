# @Author: HaoxuanLi  
# @Date 2018/11/11
# CWID: 10434197
from src.DAO.dao import Dao
from src.Domain.instructor import Instructor
from src.Utils.FileReader import FileReader


class InstructorService:
    def __init__(self):
        self.dao = Dao.get_instance()

    def save_instructor(self, instructor: Instructor):
        if not self.dao.if_exist("instructor"):
            raise Exception(f"Error: instructor table not exist")
        sql = '''insert into instructor values (?,?,?)'''
        args = (instructor.cwid, instructor.name, instructor.dept)
        self.dao.execute_sql(sql, args)

    def create_instructor_table(self, header: tuple):
        self.dao.create_table("instructor", header)

    def find_instructor(self, cwid: str):
        sql = '''select CWID, NAME, DEPT from instructor where instructor.CWID=?'''
        arg = (cwid,)
        result_tuple = self.dao.execute_sql(sql, arg)[0]
        result_ins = Instructor(result_tuple[0], result_tuple[1], result_tuple[2])
        return result_ins

    def read_instructor_from_file(self, path: str):
        if self.dao.if_exist("instructor"):
            return
        lines = FileReader.read_lines(path)
        header = [attr + " varchar(50)" for attr in lines[0]]
        header[0] += " PRIMARY KEY"
        self.create_instructor_table(tuple(header))
        for attr in lines[1:len(lines)]:
            ins = Instructor(attr[0], attr[1], attr[2])
            self.save_instructor(ins)

    def get_all_instructors(self):
        ins_list = []
        sql = '''select CWID, Name, DEPT  from instructor'''
        result_list = self.dao.execute_sql(sql)
        for result_tuple in result_list:
            ins_list.append(Instructor(result_tuple[0], result_tuple[1], result_tuple[2]))
        return ins_list
