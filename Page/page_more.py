import Page
from Base.base import Base


class Page_more(Base):
    '''更多页面操作'''

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_mobile_network_but(self):
        '''点击移动网络按钮'''
        self.click_element(Page.mobile_network_xpath)
