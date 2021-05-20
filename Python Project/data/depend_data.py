# -*- coding:utf-8 -*-
from util.study_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import parse


class DependentDate:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.get_data = GetData()

    # 通过case_id去获取case_id的值
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_rows_data(self.case_id)
        print('111111', row_num, )
        request_data = self.get_data.get_data_for_json(row_num)
        header = self.get_data.is_header(row_num)
        method = self.get_data.get_request_method(row_num)
        url = self.get_data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return res

    # 根据依赖值执行来测试case并返回
    def get_data_for_key(self, row):
        depend_data = self.get_data.get_depend_key(row)
        print('2', depend_data)
        response_data = self.run_dependent()
        print('111', response_data)
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]
