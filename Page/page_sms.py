import sys, os
sys.path.append(os.getcwd())
from Base.base import Base
from selenium.webdriver.common.by import By
import Page

class Page_sms(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_create(self):
        '''点击新建按钮'''
        self.click_element(Page.create_but)

    def input_phone(self, number):
        '''输入手机号'''
        self.send_element(Page.input_number, number)

    def input_content(self, text_content):
        '''输入短信内容'''
        self.send_element(Page.input_text_id, text_content)

    def send_but(self):
        '''点击发送按钮'''
        self.click_element(Page.send_but_id)

    def get_result(self):
        '''断言数据'''
        res_ls = self.search_elements(Page.result)
        return [i.text for i in res_ls]
