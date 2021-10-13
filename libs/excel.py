# encoding: utf-8

import xlwt
import os

class Excel():

    def __init__(self, file='default.xls', is_delete=True) -> None:
        self.book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        self.file = file
        self.is_delete = is_delete

    def __del__(self):
        if self.is_delete:
            if os.path.exists(self.file):
                os.remove(self.file)

    def save(self):
        self.book.save(self.file)

    def add_sheet(self, name:str, data:list):
        """
        制表函数
        :param name:            表单名
        :param data:            数据
        :return:
        """
        xlr = self.book.add_sheet(name, cell_overwrite_ok=True)
        i = 0
        for row in data:
            j = 0
            for field_value in row:
                if not field_value:
                    field_value = ""
                xlr.write(i, j, str(field_value))
                j += 1
            i += 1