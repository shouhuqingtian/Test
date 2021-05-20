# -*- coding:utf-8 -*-
import json
import operator
from idna import unicode


class Commonutil:
    def is_contain(self, str_one, str_two):
        flag = None
        # if isinstance(str_one, unicode):
        #     str_one = str_one.encode('utf-8').decode('utf-8')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, dict_one, dict_two):  # 判断两个字典是否相等
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_one = json.loads(dict_two)
        return operator.eq(dict_one, dict_two)
