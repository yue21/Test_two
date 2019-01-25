import Page
from Base.base import Base


class Page_network(Base):
    '''移动网络页面'''

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_one_network(self):
        '''点击首选网络类型'''
        self.click_element(Page.one_network_xpath)

    def click_set_network(self, num):
        '''设置网络'''
        if str(num) == "1":
            self.click_element(Page.set_network_3G_xpath)
        if str(num) == "2":
            self.click_element(Page.set_network_2G_xpath)

    def get_result(self):
        '''获取结果列表'''
        result_ls = self.search_elements(Page.set_network_list_ids)
        return [i.text for i in result_ls]
