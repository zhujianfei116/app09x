import pytest, sys, os

sys.path.append(os.getcwd())

from Base.page import Page
from Base.getDriver import get_android_driver


class TestSms:

    def setup_class(self):
        # 实例化统一入口类
        self.page = Page(get_android_driver("com.android.mms", ".ui.ConversationList"))

    def teardown_class(self):
        self.page.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_sms_new_page(self):
        """进入短信发送页面"""
        # 首页点击新建
        self.page.get_smshome().click_new_btn()
        # 新建短信页面输入手机号
        self.page.get_sendsms().recv_phone("13544443333")

    @pytest.mark.parametrize("text", ["hello", "world"])
    def test_sms(self, text):
        """测试短信发送"""
        # 发送
        self.page.get_sendsms().send_sms(text)
        # 取结果断言
        assert text in self.page.get_sendsms().get_sms_result()
