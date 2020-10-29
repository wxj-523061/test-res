import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import sys

from cry_sys.util.excel_operation import OperationExcel
from cry_sys.web_func.customermanage.customer_page import CustomerManager

sys.path.append('C:\\Users\\admin\\PycharmProjects\\pythonProject')
from cry_sys.web_func.usermaneger.login_page import Login


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:

        self.op = OperationExcel('../../config/test_case.xlsx','用例参数')
        self.manager = CustomerManager(self.op.get_cell(1, 1))
        # self.log = AutoLog()

    def test_customer_add_info_null(self):
        self.manager.add_new_customer(self.op.get_cell(7,2),self.op.get_cell(7,3),self.op.get_cell(7,4),self.op.get_cell(7,5))
        alert_text=self.manager.alert_text()
        self.manager.log.set_message('--获取弹出框内容--','info')
        self.assertEqual(alert_text,self.op.get_cell(7,6))

    def test_customer_add_info_must(self):
        self.manager.add_new_customer(self.op.get_cell(8,2),self.op.get_cell(8,3),self.op.get_cell(8,4),self.op.get_cell(8,5))
        alert_text=self.manager.alert_text()
        self.manager.log.set_message('--获取弹出框内容--','info')
        self.assertEqual(alert_text,self.op.get_cell(8,6))

    def test_customer_edit_info_must(self):
        self.manager.upd_customer(self.op.get_cell(9,4))
        alert_text = self.manager.alert_text()
        self.manager.log.set_message('--获取弹出框内容--', 'info')
        self.assertEqual(alert_text, self.op.get_cell(9, 6))


    def tearDown(self) -> None:
        self.manager.driver.quit()

if __name__=='__main__':
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite.addTest(test_case)
    print(time.localtime())
    # 获取当地时间
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    # 创建HTML
    with open('../../report/report_cus_' + date_now + '.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='123', description='ui_auto_test')
        runner.run(suite)
