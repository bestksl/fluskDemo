# @Author: HaoxuanLi
# @Date 2018/11/4
# CWID: 10434197
import abc


class People(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say(self):
        pass

    @abc.abstractmethod
    def pt_show(self):
        pass

