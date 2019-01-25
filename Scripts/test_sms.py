import sys, os
sys.path.append(os.getcwd())
import pytest
from appium import webdriver
from Base.initdriver import get_driver
from Page.page_sms import Page_sms


class Test_sms():
    def setup_class(self):
        self.driver = get_driver('com.android.mms', '.ui.ConversationList')
        self.page_obj = Page_sms(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    def click_create_but(self):
        self.page_obj.click_create()
        self.page_obj.input_phone('17521213144')

    @pytest.mark.parametrize('data_value', ["123", "你好", "hello"])
    def test_send_content(self, data_value):
        self.page_obj.input_content(data_value)
        self.page_obj.send_but()
        # 断言
        assert data_value in self.page_obj.get_result()
