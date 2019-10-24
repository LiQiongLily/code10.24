import yaml

with open("../data/data.yaml", "r", encoding="utf-8") as f:
    print(yaml.load(f))
