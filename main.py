import yaml
import argparse
from mainClass import imgClass

parser = argparse.ArgumentParser(description='Set up Config File')

parser = argparse.ArgumentParser()
parser.add_argument('--imagePath', type=str, default="", required= False, help='Location of image')
parser.add_argument('--matrixPath', type=str, default="", required = False , help='Location of file containing matrix')
parser.add_argument('--s', type=str, required = False , help='Filters in spatial domain separated by commas')
parser.add_argument('--f', type=str, required = False , help='Filters in frequency domain separated by commas')


args = parser.parse_args()

#Updated Configuration File
with open("configDefault.yaml") as f:
    cfg = yaml.load(f, Loader = yaml.FullLoader)

if bool(args.imagePath) is False  and bool(args.matrixPath) is False:
    print("Path must be specified")
else:
    if args.imagePath:
        cfg["imagePath"] = args.imagePath
    if args.matrixPath:
        cfg["matrixPath"] = args.matrixPath
    if args.s:
        filterList = args.s.split(",")
        for i in filterList:
            cfg["spatial"][i] = True


with open('config.yaml', "w") as f:
    yaml.dump(cfg, f)

x = imgClass(cfg)
print(x.filter)


