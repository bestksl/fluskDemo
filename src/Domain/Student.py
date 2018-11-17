# @Author: HaoxuanLi
# @Date 2018/11/4
# CWID: 10434197
from src.Interface.People import People
from src.Domain.major import Major


class Student(People):

    def say(self):
        print("Thank you professor!")

    def __init__(self, cwid: str, name: str, major_name: str):
        self.cwid = cwid
        self.name = name
        self.major_name = major_name

    def pt_show(self):
        pass
