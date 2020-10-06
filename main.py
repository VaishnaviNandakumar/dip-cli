import yaml
import argparse
import magic
from dataLoaderClass import dataLoader
from spatialFilters import filterClass

#Sample - python main.py --p C:\Users\ACER\Desktop\dip-cli\images\sample.png --s laplacian
#Parse Arguments
parser = argparse.ArgumentParser(description='Set up Config File')
parser = argparse.ArgumentParser()
parser.add_argument('--p', type=str, default="", required= False, help='Path to Image/Text file')
parser.add_argument('--dim', type=str, default="", required= False, help='Dimensions of Img/matrix')
parser.add_argument('--s', type=str, required = False , help='Filters in spatial domain separated by commas')
parser.add_argument('--f', type=str, required = False , help='Filters in frequency domain separated by commas')
args = parser.parse_args()



def callFilters(cfg):
    #Apply filters
    x = dataLoader(cfg)
    imgR = x.execute()
    obj = filterClass(cfg)
    for i in cfg["spatial"]:
        if cfg["spatial"][i] is True:
            method = getattr(obj,i)
            method(imgR)

def main():
    with open("config\configDefault.yaml") as f:          
        cfg = yaml.load(f, Loader = yaml.FullLoader)

    if bool(args.p) is False:
        print("Path must be specified")

    else:
        cfg["path"] = args.p                              
        kind = magic.from_file(cfg["path"], mime = True)  #Determine file format
        if  kind.find("image")!=-1:
            cfg["type"] = "image"
        elif kind.find("text")!=-1:
            cfg["type"] = "text"
        else:
            print("Invalid file format")

        height, width = args.dim.split("x")
        cfg["height"] = int(height)
        cfg["width"] =  int(width)

        if args.s:
            filterList = args.s.split(",")
            for i in filterList:
                cfg["spatial"][i] = True

    with open('config\config.yaml', "w") as f:              #Updated Configuration File
        yaml.dump(cfg, f)
        
    callFilters(cfg)


if __name__ == "__main__":
    main()
    


