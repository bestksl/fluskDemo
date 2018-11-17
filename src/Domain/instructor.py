# @Author: HaoxuanLi
# @Date 2018/11/4
# CWID: 10434197
from collections import defaultdict
from src.Interface.People import People


class Instructor(People):
    def say(self):
        print("Thank you professor!")

    def __init__(self, cwid: str, name: str, dept: str):
        self.cwid = cwid
        self.name = name
        self.dept = dept

    def pt_show(self):
        pass
