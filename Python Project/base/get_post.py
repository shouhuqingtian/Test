import json
import requests
import unittest


#  根据get，post自动选择
class RunMain:

    def send_get(self, url, data, headers=None):
        res = requests.get(url=url, params=data, verify=False).json()
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)

    def send_post(self, url, data, headers=None):
        res = requests.post(url=url, data=data, verify=False).json()
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)

    def run_main(self, url, method, data=None):
        if method == 'get':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    unittest.main()
