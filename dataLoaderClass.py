import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import skimage.transform as st

from spatialFilters import *

class dataLoader:
    def __init__(self, cfg):
        self.path   = cfg["path"]
        self.height = 300
        self.width  = 300
        

    def loadImage(self):
        #Loads Image
        imagePath = Image.open(self.path)
        
        #Resizes Image
        imgResize = imagePath.resize((self.height,self.width))

        #Converts to numpy array
        img = np.array(imgResize)
        self.imgPadded = np.pad(img,((1,1),(1,1),(0,0)),'constant')             

    def execute(self):
        self.loadImage()
        return self.imgPadded
        

            
            



   