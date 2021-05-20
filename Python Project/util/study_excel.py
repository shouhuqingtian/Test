# coding:utf-8
import xlrd
from xlutils3.copy import copy
# 重新封装打开Excel类
from data import data_config


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/生命科学运营平台接口.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet页内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格行数
    def get_lines(self):
        tables = self.get_data()
        return tables.nrows

    # 获取单元格内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 写入结果
    def write_result(self):
        col = int(data_config.get_result)

    # case id找行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_num(row_num)
        print(rows_data, row_num)
        return rows_data

    # case id找对应行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if str(case_id) in col_data:
                return num
            num = num + 1

    # 根据行号，找该行内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取列的值
    def get_cols_data(self, col_id=None):
        if col_id is not None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opens = OperationExcel()
    print(opens.get_lines(), opens.get_cell_value(1, 1))
