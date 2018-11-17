# @Author: HaoxuanLi  
# @Date 2018/11/10
# CWID: 10434197
import sqlite3


class Dao:
    __instance = None

    def __init__(self):
        self.db_name = "test2.db"
        self.con = None

    def open_close(func):
        def inner(self, *args):
            self.con = sqlite3.connect(self.db_name)
            cursor = self.con.cursor()
            result_list = None
            try:
                return_value = func(self, *args)
                if type(return_value) is list and type(return_value[1]) is tuple:
                    cursor.execute(return_value[0], return_value[1])
                elif type(return_value) is list and type(return_value[1]) is not tuple:
                    for sql in return_value:
                        cursor.execute(sql)
                else:
                    cursor.execute(return_value)
                result_list = cursor.fetchall()
            except Exception as e:
                self.con.rollback()
                print(f"some thing wrong: {e} and the database {self.db_name} was rollback")
                raise e
            finally:
                self.con.commit()
                self.con.close()
            return result_list

        return inner

    @open_close
    def execute_sql(self, *args):
        if len(args) == 1:
            return args[0]
        else:
            return [item for item in args]

    def if_exist(self, table_name: str):
        if self.execute_sql(f"SELECT COUNT(*) FROM sqlite_master where type='table' and name='{table_name}'")[0][
            0] == 0:
            return False
        else:
            return True

    def create_table(self, table_name: str, header: tuple):
        if self.if_exist(table_name):
            pass
        else:
            sql = f'''create table {table_name} ('''
            for i in range(0, len(header)):
                sql += f'''{header[i]},'''
            sql = sql[:-1] + ''');'''
            self.execute_sql(sql)

    @staticmethod
    def get_instance():  # save memory
        if Dao.__instance is None:
            return Dao()
        else:
            return Dao.__instance
