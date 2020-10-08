import numpy as np
import yaml
from PIL import Image
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import stats
import skimage.transform as st

class frequencyFilterClass:
    def __init__(self, cfg):
        self.h = cfg["height"]
        self.w = cfg["width"]
        self.type = cfg["type"]

    def splitChannels(self, mat, filter):
        redChannel, greenChannel, blueChannel = [] , [] , []
        for i in range(3):
            l1, l2, l3 = [] , [] , []
            for j in range(3):
                r,g,b = mat[i][j][0], mat[i][j][1], mat[i][j][2]
                
                l1.append(r)
                l2.append(g)
                l3.append(b)

                redChannel.append(l1)
                greenChannel.append(l2)
                blueChannel.append(l3)


    def gaussian(self, dist):
        D0 = 1.2
        gaussianFilter = []
        for i in range(self.h):
            for j in range(self.w):
                x = (-1*(dist[i][j]**2))/(2*(D0**2))
                gaussianFilter[i][j] = math.exp(x)


    def dft(self,matrix):
        res = np.fft.fftn(matrix)
        return res
