import numpy as np
import pandas as pd
import yaml
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import skimage.transform as st

from spatialFilters import spatialFilterClass
from frequencyFilters import frequencyFilterClass


class dataLoader:
    def __init__(self, cfg):
        self.path    = cfg["path"]
        self.height  = cfg["height"]
        self.width   = cfg["width"]
        self.type    = cfg["type"]
        self.spatial = cfg["spatial"]
        self.frequency = cfg["frequency"]
        self.objS = spatialFilterClass(cfg)
        self.objF = frequencyFilterClass(cfg)
        

    def loadImage(self):
        if self.type == "image":
            #Loads Image
            imagePath = Image.open(self.path)
            #Resizes Image
            imgResize = imagePath.resize((self.height,self.width))
            #Converts to numpy array
            self.img = np.array(imgResize)
            self.imgPadded = np.pad(self.img,((1,1),(1,1),(0,0)),'constant')    

        else:
            file = open(self.path, "r")
            matrix = []
            for row in file:
                matrix.append([int(x) for x in row.split()])
            
            self.img = np.array(matrix)
            self.imgPadded = np.pad(img, [(1, 1), (1, 1)], mode='constant')
                 

    def execute(self):
        self.loadImage()

        if self.spatial:
            for i in self.spatial:
                if self.spatial[i] is True:
                    method = getattr(self.objS,i)
                    method(self.imgPadded)
        
        if self.frequency:
            for i in self.frequency:
                if self.frequency[i] is True:
                    method = getattr(self.objF,i)
                    method(self.img)
        
        

            
            



   