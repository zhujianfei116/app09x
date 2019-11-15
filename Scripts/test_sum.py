import pytest, yaml, os, sys

sys.path.append(os.getcwd())

from Base.getData import GetData


def get_data():
    """读yaml文件数据"""
    lis = []
    # data = GetData.get_yml_data("sum.yml")  # 静态方法调用
    data = GetData().get_yml_data("sum.yml")
    for i in data.values():
        lis.append(tuple(i.values()))
    return lis


"""
data = {
    'test_001': {'a': 1, 'b': 2, 'c': 3}, 
    'test_002': {'a': 2, 'b': 3, 'c': 5}, 
    'test_003': {'a': 5, 'b': 6, 'c': 7}
}
# 1。取所有data.values = [{'a': 1, 'b': 2, 'c': 3},{'a': 2, 'b': 3, 'c': 5}..]
# 2.遍历步骤1结果，取每个值的values [1,2,3] [2,3,5] [5,6,7]
# 3.将步骤2列表转元组
# 4。将步骤3的所有结果方法列表中
"""


class TestSum:
    # @pytest.mark.parametrize("a,b,c", [(1, 2, 3), (2, 3, 5), (5, 6, 7)])
    @pytest.mark.parametrize("a,b,c", get_data())
    def test_sum(self, a, b, c):
        """计算两个数的和等于第三个数"""

        assert a + b == c
