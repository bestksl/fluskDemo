# @Author: HaoxuanLi  
# @Date 2018/11/12
# CWID: 10434197
# @Author: HaoxuanLi
# @Date 2018/11/11
# CWID: 10434197
from src.DAO.dao import Dao
from src.Domain.major import Major


class MajorService:
    def __init__(self):
        self.dao = Dao.get_instance()

    def save_major(self, major_name: str, course_name: str):
        if not self.dao.if_exist("major"):
            raise Exception(f"Error: major table not exist")
        sql = '''insert into Major values (?,?)'''
        args = (major_name, course_name)
        self.dao.execute_sql(sql, args)

    def create_major_table(self, header: tuple):
        self.dao.create_table("major", header)

    def find_courses(self, major_name: str):
        sql = '''select  Course from major where major.Major=?'''
        arg = (major_name,)
        result_tuple = self.dao.execute_sql(sql, arg)
        result_list = [course_tuple[0] for course_tuple in result_tuple]
        return result_list
