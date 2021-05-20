# -*- coding:utf-8 -*-
import requests
import json
from util.operation_json import OperationJson


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    # 获取登录返回的token的url
    def get_response_url(self):
        url = self.response['data']['url'][0]
        return url

    # 获取cookie的jar文件
    def get_cookie(self):
        url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie

    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OperationJson()
        op_json.write_data(cookie)


if __name__ == '__main__':
    url = 'http://api3.top-human.com/p/admin/login'
    data = {
        "username": "benefmAdmin",
        "password": "123456"
    }
    res = json.dumps(requests.post(url, data).json())
    op_header = OperationHeader(res)
    op_header.write_cookie()
'''
url = 'http://api3.top-human.com/p/admin/login'
home_url = 'http://ecg_management.benefm.com/#/index'
data = {
    "username": "benefmAdmin",
    "password": "123456"
}
data = json.dumps(data)
headers = {
    'Content-Type': 'application/json;charset=UTF-8'
}

response = requests.post(url, data, headers=headers).json()
token = response['resultData']['access_token']
cookie = requests.get(home_url).cookies
cook_jar = requests.utils.cookiejar_from_dict(cookie)
print(type(cookie), type(cook_jar))
'''