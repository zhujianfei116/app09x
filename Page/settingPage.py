from Base.base import Base
from Page.pageElements import PageElements


class SettingPage(Base):
    """设置页面所有方法声明"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_ele(PageElements.search_btn)
