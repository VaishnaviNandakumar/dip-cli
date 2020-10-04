import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import skimage.transform as st
h= 300
w= 300

#Laplacian Filter
laplacianFilter = np.array([[0,1,0],[1,-4,1],[0,1,0]])

#Sobel Filter
sobelX = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobelY = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

#Prewitt Filter
prewittX =  np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
prewittY = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])


class filterClass:
    def conv(self,mat1, mat2):
        val = np.dot(mat1, mat2)
        return np.sum(val)

    def splitChannels(self, mat, filter):
        redChannel = []
        greenChannel = []
        blueChannel = []
        for i in range(3):
            l1 = []
            l2 = []
            l3 = []
            for j in range(3):
                r = mat[i][j][0]
                g = mat[i][j][1]
                b = mat[i][j][2]
                l1.append(r)
                l2.append(g)
                l3.append(b)
                redChannel.append(l1)
                greenChannel.append(l2)
                blueChannel.append(l3)
        #print(redChannel)
        #print(greenChannel)
        #print(blueChannel)
        x = self.conv(redChannel, filter)
        y = self.conv(greenChannel, filter)
        z = self.conv(blueChannel, filter)
        return x, y, z


    #Main Function - Laplace Filter
    def laplacian(self, imgPadded):
        #print("reached laplacian")
        filter = laplacianFilter
        ans = []
        for i in range(0, w-2):
            temp = []
            for j in range(0, h-2):
                mat = []
                for k in range(i, i+3):
                    l = []
                    for q in range(j, j+3):
                        l.append(imgPadded[k][q])
                    mat.append(l)

                val = self.splitChannels(mat, filter)
                
                x = list(val)
                #print(i,j)
                temp.append(x)
            ans.append(temp)
        plt.imshow(ans)
        plt.show()


    #Main Function - Sobel Filter
    def sobel(self,imgPadded): 
        #Setting Filter
        filterX = sobelX
        filterY = sobelY
        ans = []
        for i in range(0, w-2):
            temp = []
            for j in range(0, h-2):
                mat = []
                for k in range(i, i+3):
                    l = []
                    for q in range(j, j+3):
                        l.append(imgPadded[k][q])
                    mat.append(l)

                val1 = self.splitChannels(mat, filterX)
                val2 = self.splitChannels(mat, filterY)
                
                x = np.add(list(val1), list(val2))
                
                #print(i,j)
                temp.append(x)
            ans.append(temp)
        plt.imshow(ans)
        plt.show()


    #Main Function - Prewitt Filter
    def prewitt(imgPadded): 
        #Setting Filter
        filterX = prewittX
        filterY = prewittY
        ans = []
        for i in range(0, w-2):
            temp = []
            for j in range(0, h-2):
                mat = []
                for k in range(i, i+3):
                    l = []
                    for q in range(j, j+3):
                        l.append(imgPadded[k][q])
                    mat.append(l)

                val1 = splitChannels(mat, filterX)
                val2 = splitChannels(mat, filterY)
                
                x = np.add(list(val1), list(val2))
                
                #print(i,j)
                temp.append(x)
            ans.append(temp)
        #plt.imshow(ans)
        #Conversion to grayscale
        def rgb2gray(rgb):
            return np.dot(rgb[::3], [0.2989, 0.5870, 0.1140])

        gray = np.array(rgb2gray(ans))
        #plt.imshow(st.resize(gray, (300, 300)), cmap=plt.get_cmap('gray'))
