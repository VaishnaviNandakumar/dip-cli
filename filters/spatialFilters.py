from base import *

class spatialFilterClass:
    
    def __init__(self, cfg):
        self.cfg = cfg
        self.h = cfg["height"]
        self.w = cfg["width"]
        
        
    def conv(self,mat1, mat2):
        val = np.dot(mat1, mat2)
        return np.sum(val)

    def statFilter(self, mat, filter):
        redChannel, greenChannel, blueChannel = splitChannels(mat, 3,3)       
        if filter == "max":
            x  = np.array(redChannel).max()
            y  = np.array(greenChannel).max()
            z  = np.array(blueChannel).max()

        elif filter == "min":
            x  = np.array(redChannel).min()
            y  = np.array(greenChannel).min()
            z  = np.array(blueChannel).min()
        
        elif filter == "median":
            x  = int(np.median(redChannel))
            y  = int(np.median(greenChannel))
            z  = int(np.median(blueChannel))
            
        elif filter == "mean":
            x  = int(np.mean(redChannel))
            y  = int(np.mean(greenChannel))
            z  = int(np.mean(blueChannel))

        else:
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

                if self.cfg["type"] == "image":
                    val = self.statFilter(mat, filter)
                    x = list(val)
                else:
                    val = self.conv(mat,filter)
                    x = val
                temp.append(x)
            ans.append(temp)

        return ans
        

    def laplacian(self, imgPadded):
        #Laplacian Filter
        laplacianFilter = np.array([[0,1,0],[1,-4,1],[0,1,0]])
        filter = laplacianFilter
        return self.block(imgPadded, filter)
        
    def sobel(self,imgPadded): 
        #Sobel Filter
        sobelX = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
        sobelY = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        filterX = sobelX
        filterY = sobelY
        val1 = self.block(imgPadded, filterX)
        val2 = self.block(imgPadded, filterY)        
        return np.add(val1, val2) 
       
   
    def prewitt(self,imgPadded): 
        #Prewitt Filter
        prewittX =  np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
        prewittY = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        filterX = prewittX
        filterY = prewittY
        val1 = self.block(imgPadded, filterX)
        val2 = self.block(imgPadded, filterY)        
        return np.add(val1, val2)  
           
    def max(self, imgPadded):
        filter = "max"
        return self.block(imgPadded, filter)
          
    def min(self, imgPadded):
        filter = "min"
        return self.block(imgPadded, filter)
       

    def median(self, imgPadded):
        filter = "median" 
        return self.block(imgPadded, filter)
        
    def avg(self, imgPadded):
        filter = "mean"
        return self.block(imgPadded, filter)



