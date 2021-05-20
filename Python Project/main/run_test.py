# -*- coding:utf-8 -*-
import sys
env_variable = [r'D:\Python Project\main',
                r'D:\Python Project',
                r'C:\Program Files\JetBrains\PyCharm 2020.1.2\plugins\python\helpers\pycharm_display',
                r'D:\Python Project\venv\Scripts\python37.zip',
                r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\DLLs',
                r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib',
                r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37',
                r'D:\Python Project\venv',
                r'D:\Python Project\venv\lib\site-packages',
                r'C:\Users\Administrator\AppData\Roaming\Python\Python37\site-packages',
                r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib\site-packages',
                r'C:\Program Files\JetBrains\PyCharm 2020.1.2\plugins\python\helpers\pycharm_matplotlib_backend',
                r'D:\Python Project',
                r'D:\Python Project\venv\lib\site-packages',
                r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages',
                r'C:\Users\Administrator\AppData\Roaming\Python\Python37\site-packages']
sys.path.extend(env_variable)
import urllib3
from base.runmethod import RunMethod
from data.get_data import GetData
from util.commonutil import Commonutil
import json
from data.depend_data import DependentDate
from util.send_email import SendEmail
from util.operation_json import OperationJson
from util.operation_header import OperationHeader

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.commonutil = Commonutil()
        self.sendmail = SendEmail()

    def go_on_run(self):  # 程序执行
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data_for_json(i)
                # expect = self.data.get_expect_data(i)  # Excel写入预期结果
                expect = self.data.get_expect_data_for_mysql(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                res = self.run_method.run_main(method, url, data, header)
                values = {"resultCode": res["resultCode"]}
                # print(res["resultData"]["access_id"])
                value = json.dumps(values)  # 字典转字符串匹配
                if depend_case is not None:
                    self.depend_data = DependentDate(depend_case)
                    # 依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    data = json.loads(data)
                    depend_key = self.data.get_depend_field(i)
                    data[depend_key] = depend_response_data
                if header == 'write':
                    res = self.run_method.run_main(method, url, data)
                    op_header = OperationHeader(res)
                    op_header.write_cookie()

                elif header == 'yes':
                    op_json = OperationJson('../dataconfig/cooking.json')
                    cookie = op_json.get_data('apsid')
                    cookies = {
                        'apsid': cookie
                    }
                    value = self.run_method.run_main(method, url, data, cookies)
                else:
                    value = self.run_method.run_main(method, url, data)
                if self.commonutil.is_equal_dict(expect, value):
                    self.data.write_result(i, '通过')
                    pass_count.append(i)
                    print('测试通过')
                else:
                    self.data.write_result(i, '失败')
                    fail_count.append(i)
                    print('测试失败')

                print(pass_count, fail_count)
        self.sendmail.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

