# -*- coding:utf-8 -*-
import requests
import json


# 重构主方法
class RunMethod:
    def post_main(self, url, data, header=None):
        if header is not None:
            res = requests.post(url=url, data=data, headers=header, verify=False).json()
        else:
            res = requests.post(url=url, data=data, verify=False).json()
        return res

    def get_main(self, url, data, header=None):
        if header is not None:
            res = requests.get(url=url, data=data, headers=header, verify=False).json()
        else:
            res = requests.get(url=url, data=data, verify=False).json()
        return res

    def run_main(self, method, url, data=None, header=None):
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        # return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        return res
