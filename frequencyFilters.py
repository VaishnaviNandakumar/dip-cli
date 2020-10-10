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

    def splitChannels(self, mat):
        redChannel, greenChannel, blueChannel = [] , [] , []
        for i in range(self.h):
            l1, l2, l3 = [] , [] , []
            for j in range(self.w):
                r,g,b = mat[i][j][0], mat[i][j][1], mat[i][j][2]
                
                l1.append(r)
                l2.append(g)
                l3.append(b)

            redChannel.append(l1)
            greenChannel.append(l2)
            blueChannel.append(l3)
        return redChannel, greenChannel, blueChannel

    def gaussian(self, dist):
        D0 = 40
        gaussianFilter = []
        for i in range(self.h):
            l = []
            for j in range(self.w):
                x = ((dist[i][j]**2))/(2*(D0**2))
                val = math.exp(-x)
                l.append(val)
            gaussianFilter.append(l)
        
        return gaussianFilter

    def mul(self, matrix):
        for i in range(self.h):
            for j in range(self.w):
                matrix[i][j]*=pow((-1),(i+j))
        return matrix

    def dft(self,matrix):
        res = np.fft.fftn(matrix)
        return res

    def idft(self,matrix):
        res = np.fft.ifftn(matrix)
        return res

    def distCalc(self, h,w):
        dist = []
        n = int(h/2)
        for i in range(n,-n-1,-1):
            l = []
            for j in range(-n,n+1,1):
                l.append(math.sqrt(i**2+j**2))
            dist.append(l)

        return dist   


    def start(self, img):
    
        if self.type =="image":
            r,g,b = self.splitChannels(img)
            r = self.dft(self.mul(r))
            g = self.dft(self.mul(g))
            b = self.dft(self.mul(b))
            
            dist = self.distCalc(self.h,self.w)
            M = self.gaussian(dist) 
            
            x = self.mul(self.idft(np.multiply(r,M)).real)
            y = self.mul(self.idft(np.multiply(g,M)).real)
            z = self.mul(self.idft(np.multiply(b,M)).real)
            
            op = img
            for i in range(self.h):
                for j in range(self.w):
                    op[i][j][0] = int(x[i][j])
                    op[i][j][1] = int(y[i][j])
                    op[i][j][2] = int(z[i][j])
              
            plt.imshow(op)
            plt.show()

            
        else:
            img  = self.dft(img)
            dist = self.distCalc(self.h,self.w)
            #print("Distance", dist)
            x = self.gaussian(dist)
            #print('Filter', x)
            y = np.multiply(x,img)
            ift = self.idft(y)
            z = ift.real
            ans = self.mul(z)
            #print(ans)
            plt.imshow(ans)
            plt.show()

