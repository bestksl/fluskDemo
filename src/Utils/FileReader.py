# @Author: HaoxuanLi
# @Date 2018/11/4
# CWID: 10434197


class FileReader:
    @staticmethod
    def read_lines(path: str):
        lines = []
        try:
            file = open(path)
        except FileNotFoundError:
            raise FileNotFoundError(f'warning: file({path}) not found')
        with file:
            for line in file:
                attr = line.strip().split(f"\t")
                if len(attr) != 0 or attr is not None:
                    lines.append(attr)
                else:
                    break
        return lines
