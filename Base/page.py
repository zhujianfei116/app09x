from Page.sendSmsPage import SenSmsPage
from Page.smsHomePage import SmsHome
from Page.settingPage import SettingPage
from Page.searchPage import SearchPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_smshome(self):
        """返回短信首页"""
        return SmsHome(self.driver)

    def get_sendsms(self):
        """返回短信发送页面"""
        return SenSmsPage(self.driver)

    def get_setting(self):
        """返回设置页面对象"""
        return SettingPage(self.driver)

    def get_search(self):
        """返回搜索页面对象"""
        return SearchPage(self.driver)
