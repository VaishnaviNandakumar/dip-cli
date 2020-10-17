from base import *

class frequencyFilterClass:
    def __init__(self, cfg):
        self.cfg = cfg
        self.h = cfg["height"]
        self.w = cfg["width"]
        
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
    
    def  butterworth(self, dist):
        D0 = 20
        n = 1.2
        butterworthFilter = []
        for i in range(self.h):
            l = []
            for j in range(self.w):
                x = (dist[i][j]/D0)**(2*n)
                val = 1/(1+x)
                l.append(val)
            butterworthFilter.append(l)
        return butterworthFilter
    
        def ideal(self, dist):
            #D0 = 20 cool stuff
            D0 = 10
            idealFilter = []
            for i in range(self.h):
                l = []
                for j in range(self.w):
                    if dist[i][j]>=D0:
                        val = 1
                    else:
                        val = 0
                    l.append(val)
                idealFilter.append(l)
            return idealFilter

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
    
    def start(self, img, filter):
        dist = self.distCalc(self.h,self.w)

        if filter == "gaussian":
            M = self.gaussian(dist)
        elif filter == "butterworth":
            M = self.butterworth(dist)
        elif filter == "ideal":
            M = self.ideal(dist)
            
        if self.cfg["type"] =="image":
            r,g,b = splitChannels(img, self.h, self.w)
            r = self.dft(self.mul(r))
            g = self.dft(self.mul(g))
            b = self.dft(self.mul(b))
        
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
            img  = self.dft(self.mul(img))
            op = self.mul(self.idft(np.multiply(img,M)).real)
            print(op)
            plt.imshow(op)
            plt.show()

            

     
