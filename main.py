import argparse

parser = argparse.ArgumentParser(description='Apply filters')

parser = argparse.ArgumentParser()
parser.add_argument('--config_path', type=str, default="", required= True, help='Location of current config file')
parser.add_argument('--dataset_csvpath', type=str, required=True, default="./", help='Location to data csv file')

args = parser.parse_args()
print("Config Path", args.config_path)
print("Dataset CSV Path", args.dataset_csvpath)