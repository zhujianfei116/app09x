import yaml, os


class GetData:

    # @staticmethod  # 装饰一个方法为静态方法，方法不需要传入self
    # def get_yml_data(name):
    def get_yml_data(self, name):
        """
        返回yaml文件数据
        :param name: yaml文件名字
        :return: 返回yaml文件数据
        """
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            # 解析yaml数据
            return yaml.safe_load(f)

    def get_csv_data(self):
        pass

    def get_mysql_data(self):
        pass
