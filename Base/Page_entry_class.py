from Page.page_setting import Page_setting
from Page.page_more import Page_more
from Page.page_network import Page_network


class Page_entry_class:
    def __init__(self, driver):
        self.driver = driver

    def get_page_setting_obj(self):
        return Page_setting(self.driver)

    def get_page_more_obj(self):
        return Page_more(self.driver)

    def get_page_network_obj(self):
        return Page_network(self.driver)
