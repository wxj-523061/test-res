import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import sys
sys.path.append('E:\\pythonProject1')
from cry_sys.web_func.usermaneger.login_page import Login
from cry_sys.util.excel_operation import OperationExcel

class TestLogin(unittest.TestCase):

    def setUp(self) -> None:

        self.op = OperationExcel('../../config/test_case.xlsx','用例参数')
        self.login = Login(self.op.get_cell(1, 1))
        # self.log = AutoLog()

    def test_login_name_passwd_null(self):
        self.login.login(self.op.get_cell(1,2),self.op.get_cell(1,3))
        alert_text=self.login.alert_text()
        self.login.log.set_message('--获取弹出框内容--','info')
        self.assertEqual(alert_text,self.op.get_cell(1,4))

    def test_login_passwd_null(self):
        self.login.login(self.op.get_cell(2,2),self.op.get_cell(2,3))
        alert_text=self.login.alert_text()
        self.login.log.set_message('--获取弹出框内容--','info')
        self.assertEqual(alert_text,self.op.get_cell(2,4))

    def test_login_name_null(self):
        self.login.login(self.op.get_cell(3,2),self.op.get_cell(3,3))
        alert_text=self.login.alert_text()
        self.login.log.set_message('--获取弹出框内容--','info')
        self.assertEqual(alert_text,self.op.get_cell(3,4))

    def test_login_name_password_error(self):
        self.login.login(self.op.get_cell(4,2),self.op.get_cell(4,3))
        alert_text=self.login.alert_text()
        self.login.log.set_message('--获取弹出框内容--','info')
        self.assertEqual(alert_text,self.op.get_cell(4,4))
    #
    def test_login_success(self):
        self.login.login(self.op.get_cell(5, 2), int(self.op.get_cell(5, 3)))
        self.re=self.login.frame_text()
        self.assertEqual(self.re, self.op.get_cell(5,4))

    def tearDown(self) -> None:
        self.login.driver.quit()

if __name__=='__main__':
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite.addTest(test_case)
    print(time.localtime())
    # 获取当地时间
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    # 创建HTML
    with open('../../report/report_login' + '.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='123', description='ui_auto_test')
        runner.run(suite)
