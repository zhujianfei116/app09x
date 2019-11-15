from selenium.webdriver.common.by import By

from Base.base import Base
from Page.pageElements import PageElements


class SearchPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def search_text(self, text):
        """
        搜索内容
        :param text: 搜索具体内容
        :return:
        """
        self.send_ele(PageElements.search_input, text)

    def get_search_result(self):
        """获取搜索结果列表"""
        # 定位所有搜索结果
        results = self.search_eles(PageElements.search_result)
        # 返回搜索结果列表文本
        return [i.text for i in results]
