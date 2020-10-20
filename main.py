import yaml
import argparse
import magic
from dataLoaderClass import dataLoader
from filters.spatialFilters import spatialFilterClass
from filters.frequencyFilters import frequencyFilterClass

parser = argparse.ArgumentParser(description='Set up Config File')   
parser = argparse.ArgumentParser()
parser.add_argument('--p', type=str, default="", required= False, help='Path to Image/Text file')
parser.add_argument('--dim', type=str, default="", required= False, help='Dimensions of Img/matrix')
parser.add_argument('--s', type=str, required = False , help='Filters in spatial domain separated by commas')
parser.add_argument('--f', type=str, required = False , help='Filters in frequency domain separated by commas')
parser.add_argument('--d', required = False , help='Store threshold value for frequency filter')
parser.add_argument('--n', required = False , help='Store n value for frequency filter')
parser.add_argument('--save', required = False , action='store_true', help='To save output file or not')
args = parser.parse_args()

def main():
    with open("config\configDefault.yaml") as f:          
        cfg = yaml.load(f, Loader = yaml.FullLoader)

    if bool(args.p) is False:
        print("Path must be specified")
    else:
        cfg["path"] = args.p                              
        try :
            kind = magic.from_file(cfg["path"], mime = True)  #Determine file format
            if  kind.find("image")!=-1:
                cfg["type"] = "image"
            elif kind.find("text")!=-1:
                cfg["type"] = "text"
        except FileNotFoundError:
            print("Invalid file format")
            return

        try:
            if args.dim:
                height, width = args.dim.split("x")
                cfg["height"] = int(height)
                cfg["width"] =  int(width)
        except (TypeError,ValueError):
            print("Incorrect Dimensions")
            return

        if args.s:
            filterList = args.s.split(",")
            for i in filterList:
                cfg["spatial"][i] = True
        elif args.f:
            filterList = args.f.split(",")
            for i in filterList:
                cfg["frequency"][i] = True
         
        if args.save:
            cfg["save"] = True
        
        if bool(args.d):
            cfg["frequency"]["d"] = args.d
        
        if bool(args.n):
            cfg["frequency"]["n"] = args.n

    with open('config\config.yaml', "w") as f:              #Updated Configuration File
        yaml.dump(cfg, f)
        
    x = dataLoader(cfg)
    x.execute()


if __name__ == "__main__":
    main()
    


