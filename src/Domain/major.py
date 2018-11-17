# @Author: HaoxuanLi  
# @Date 2018/11/4
# CWID: 10434197
class Major:
    def __init__(self, name: str):
        self.name = name
        self.courses = dict()

    def add_course(self, course_name: str, type: str):
        self.courses[course_name] = type

    def get_remaining_courses(self, stu_courses: dict):
        remaining_dict = dict()
        for course_name in self.courses.keys():
            if course_name not in stu_courses.keys():
                remaining_dict[course_name] = self.courses[course_name]
        return remaining_dict

    def pt_show(self):
        return [self.name, [course for course in self.courses.keys() if self.courses[course] is "R"],
                [course for course in self.courses.keys() if self.courses[course] is "E"]]

    @staticmethod
    def get_field_name():
        return ["DEPT", "Required", "Electives"]
