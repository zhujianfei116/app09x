import pytest, sys, os

"""必须要在导入自定义包之前声明"""
sys.path.append(os.getcwd())

from Base.page import Page
from Base.getDriver import get_android_driver
from Base.getData import GetData


def search_data():
    """组装搜索测试数据"""
    # [("1", "休眠"), ("m", "MAC地址"), ("w", "WPS按钮")]
    # 存储数据列表
    search_value = []
    data = GetData().get_yml_data("search.yml")
    for i in data.values():
        search_value.append(tuple(i.values()))
    return search_value


class TestSearch:

    def setup_class(self):
        # 声明driver
        self.driver = get_android_driver('com.android.settings', '.Settings')

        # 实例化统一入口页面类
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def click_search(self):
        """点击搜索按钮 依赖一次"""
        self.page_obj.get_setting().click_search_btn()

    @pytest.mark.parametrize("search, expdata", search_data())
    def test_search(self, search, expdata):
        """
        搜索测试
        :param search: 搜索内容
        :param expdata: 搜索预期结果
        :return:
        """
        # # 定位搜索输入框
        self.page_obj.get_search().search_text(search)
        # 断言
        assert expdata in self.page_obj.get_search().get_search_result()
