# 导包
import yaml

# 写入文件流并调用dump 方法
with open("../data/write.yaml", "w", encoding="utf-8") as f:
    data = {"name": "张三", "age": 18}
    yaml.dump(data, f, allow_unicode=True)

