import yaml

with open(r'config.yaml') as file:
    cfg = yaml.load(file, Loader=yaml.FullLoader)
    print(cfg['imagePath'])