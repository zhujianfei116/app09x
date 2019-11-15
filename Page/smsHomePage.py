from Base.base import Base
from Page.pageElements import PageElements


class SmsHome(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_new_btn(self):
        """点击短信新建按钮"""
        self.click_ele(PageElements.home_new_btn_id)
