import numpy as np
import yaml
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import skimage.transform as st


    
class filterClass:

    def __init__(self, cfg):
        self.h = cfg["height"]
        self.w = cfg["width"]
        self.type = cfg["type"]
 
    def conv(self,mat1, mat2):
        val = np.dot(mat1, mat2)
        return np.sum(val)

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
        
        x = self.conv(redChannel, filter) 
        y = self.conv(greenChannel, filter) 
        z = self.conv(blueChannel, filter)

        return x, y, z

    def block(self, imgPadded, filter):

        ans = []

        for i in range(0, self.h):
            temp = []

            for j in range(0, self.w):

                mat = []
                for k in range(i, i+3):

                    l = []
                    for q in range(j, j+3):
                        l.append(imgPadded[k][q])
                    mat.append(l)

                if self.type == "image":
                    val = self.splitChannels(mat, filter)
                    x = list(val)
                else:
                    val = self.conv(mat,filter)
                    x = val
                temp.append(x)
            ans.append(temp)

        return ans
        

    #Main Function - Laplace Filter
    def laplacian(self, imgPadded):
        #Laplacian Filter
        laplacianFilter = np.array([[0,1,0],[1,-4,1],[0,1,0]])
        filter = laplacianFilter
        answer = self.block(imgPadded, filter)
        plt.imshow(answer)
        #print(ans)
        plt.show()


    #Main Function - Sobel Filter
    def sobel(self,imgPadded): 
        #Sobel Filter
        sobelX = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
        sobelY = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

        #Setting Filter
        filterX = sobelX
        filterY = sobelY
        
        val1 = self.block(imgPadded, filterX)
        val2 = self.block(imgPadded, filterX)        
        answer = np.add(val1, val2)  
        plt.imshow(answer)
        plt.show()


    #Main Function - Prewitt Filter
    def prewitt(self,imgPadded): 
        #Prewitt Filter
        prewittX =  np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
        prewittY = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        #Setting Filter
        filterX = prewittX
        filterY = prewittY

        val1 = self.block(imgPadded, filterX)
        val2 = self.block(imgPadded, filterX)        
        answer = np.add(val1, val2)  
        plt.imshow(answer)
        plt.show()
    
    #Conversion to grayscale
    '''def rgb2gray(rgb):
        return np.dot(rgb[::3], [0.2989, 0.5870, 0.1140])
        gray = np.array(rgb2gray(ans))
        #plt.imshow(st.resize(gray, (300, 300)), cmap=plt.get_cmap('gray'))
    '''