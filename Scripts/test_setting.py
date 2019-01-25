import sys, os, pytest

sys.path.append(os.getcwd())
from Base.Page_entry_class import Page_entry_class
from Base.initdriver import get_driver


class Test_setting:
    def setup_class(self):
        self.driver = get_driver('com.android.settings', '.Settings')
        self.page_entry_class_obj = Page_entry_class(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def click_more_and_mobile_network(self):
        '''点击更多和移动网络'''
        self.page_entry_class_obj.get_page_setting_obj().click_more_but()
        self.page_entry_class_obj.get_page_more_obj().click_mobile_network_but()

    def test_set_network(self):
        '''点击网络类型选择3G'''
        self.page_entry_class_obj.get_page_network_obj().click_one_network()
        self.page_entry_class_obj.get_page_network_obj().click_set_network(1)
        '''断言'''
        assert "3G" in self.page_entry_class_obj.get_page_network_obj().get_result()
