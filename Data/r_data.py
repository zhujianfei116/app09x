import yaml

with open("./data.yaml", "r") as f:
    # yaml加载数据
    data = yaml.safe_load(f)
    # 打印读取内容
    print(data)
    # print(type(data.get("no2")))
    # print(type(data.get("flox")))
