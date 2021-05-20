import unittest
from base.get_post import RunMain
import json
import mock
from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner
from base.study_mock import mock_test


# 导入自定义重写框架
class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = 'http://api.mymagicangel.com/users/admin/userinfo'
        data = {
            'appKey': 'almond',
            'phoneNumber': 18575588381
        }
        # self.run.run_main = mock.Mock(return_value=data)+
        # res = self.run.run_main(url, 'get', data)
        print(self.run.run_main)
        res = mock_test(url, 'get', data, '老铁666')
        globals()['name'] = 500
        # result = json.loads(res)
        # self.assertEqual(result['resultCode'], '200', '测试失败')
        self.assertTrue(res)
        print('第一个测试计划', res)

    # @unittest.skip('test02')
    def test_02(self):
        url = 'http://api.mymagicangel.com/users/admin/userinfo'
        data = {
            'appKey': 'almond',
            'phoneNumber': 18681015703
        }
        self.run.run_main = mock.Mock(return_value=url)
        res = self.run.run_main(url, 'get', data)
        self.assertTrue(True, '测试通过')
        print('第二个测试计划', res)

    def tearDown(self):
        print('-------------', '你好')


# 测试集，用TestRunnner输出报告
if __name__ == '__main__':
    # filepath = '../case/report.html'
    with open('../case/report.html', 'w', encoding='utf-8') as file:
        suite = unittest.TestSuite()
        suite.addTest(TestMethod('test_01'))
        suite.addTest(TestMethod('test_02'))
        runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='this is first report')
        runner.run(suite)
