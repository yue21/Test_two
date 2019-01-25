import Page
from Base.base import Base


class Page_setting(Base):
    '''设置页面'''

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_more_but(self):
        '''点击更多按钮'''
        self.click_element(Page.more_btn_xpath)
