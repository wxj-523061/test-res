import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from cry_sys.config.log_crm import AutoLog
from cry_sys.util.yaml_operation import YamlOperation


class CustomerManager():

    def __init__(self,url):
        self.log=AutoLog()
        self.driver = webdriver.Chrome('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(url)
        time.sleep(2)
        self.yo = YamlOperation('../../config/locator.yaml')

    def add_new_customer(self,customer_name,customer_data,customer_email,edit_peple):
        self.element_one = self.driver.find_element_by_name('userNum')
        self.element_one.send_keys('admin')
        self.element_two = self.driver.find_element_by_name('userPw')
        self.element_two.send_keys('123456')
        time.sleep(3)
        self.element_three = self.driver.find_element_by_id('in1').click()
        self.log.set_message('添加客户信息开始', 'info')
        self.driver.switch_to.frame('topFrame')
        time.sleep(3)
        self.customer_message = self.driver.find_element_by_link_text('客户信息')
        self.customer_message.click()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('mainFrame')
        self.driver.find_element_by_xpath(
            '/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input').click()
        # self.driver.switch_to.parent_frame()
        time.sleep(3)
        self.driver.find_element_by_name('customerName').send_keys(customer_name)
        self.driver.find_element_by_name('customerBirthday').click()
        self.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.driver.find_element_by_id('customerBirthday').clear()
        self.driver.find_element_by_id('customerBirthday').send_keys(customer_data)
        time.sleep(3)
        self.driver.find_element_by_name('customerEmail').send_keys(customer_email)
        time.sleep(3)
        self.driver.find_element_by_name('customerAddMan').send_keys(edit_peple)
        time.sleep(3)
        # self.driver.execute_async_script("document.getElementById('customerBirthday').value='2000-10-24 11:31:52'")
        self.driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td[2]/input').click()
        self.log.set_message('添加客户完成', 'info')

    def upd_customer(self,email):
        element_one = self.driver.find_element_by_name('userNum')
        element_one.send_keys('admin')
        element_two = self.driver.find_element_by_name('userPw')
        element_two.send_keys('123456')
        self.driver.find_element_by_id('in1').click()
        self.log.set_message('admin登录成功', 'info')
        self.driver.switch_to.frame('topFrame')
        time.sleep(3)
        self.driver.find_element_by_link_text('客户信息').click()
        time.sleep(3)
        self.log.set_message('成功进入客户信息界面', 'info')
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('mainFrame')
        element_four = self.driver.find_element_by_link_text('编辑')
        element_four.click()
        self.log.set_message('成功进入客户信息编辑界面', 'info')
        time.sleep(3)
        element_five = self.driver.find_element_by_name('customerEmail')
        element_five.send_keys(email)
        self.log.set_message('客户的邮箱修改', 'info')
        time.sleep(3)
        self.driver.find_element_by_name('submit').click()
        self.log.set_message('客户信息修改成功', 'info')

    def alert_text(self):
        alert = Alert(self.driver)
        return alert.text

# if __name__ == '__main__':
#     cus=CustomerManager('http://localhost:8080/crm/')
#     cus.add_new_customer_must()


