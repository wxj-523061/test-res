import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from cry_sys.config.log_crm import AutoLog
# from cry_sys.util.yaml_operation import YamlOperation


class Login:

    def __init__(self,url):
        self.log=AutoLog()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        time.sleep(5)
        # self.yo=YamlOperation('../../config/locator.yaml')


    def login(self,username,password):

        self.log.set_message('登录功能开始','info')
        username_e = self.driver.find_element_by_name('userNum')
        username_e.send_keys(username)
        time.sleep(3)
        self.log.set_message('-----输入用户名-----','info')
        password_o = self.driver.find_element_by_name('userPw')
        password_o.send_keys(password)
        time.sleep(3)
        self.log.set_message('-----输入密码-----','info')
        self.driver.find_element_by_xpath('//*[@id="in1"]').click()
        time.sleep(3)
        self.log.set_message('--点击登录--','info')

    def alert_text(self):
        alert = Alert(self.driver)
        return alert.text

    def frame_text(self) -> object:
        self.driver.switch_to.frame('topFrame')
        new_page=self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div').text
        return new_page
