# -*- coding:utf-8 -*-
import json


class OperationJson:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = '../dataconfig/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json
    def read_data(self):
        with open(self.file_path, encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        # return self.data[id]
        data = self.data[id]
        string_data = json.dumps(data)
        return string_data


if __name__ == '__main__':
    opjson = OperationJson()
    json_value = opjson.get_data('shop')
    # for i in json_value:
    #     print(i['high'])
    b = [j for i in json_value for j in i]
    print(json_value)
