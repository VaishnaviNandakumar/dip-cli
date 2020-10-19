from base import *
from filters.spatialFilters import spatialFilterClass
from filters.frequencyFilters import frequencyFilterClass


class dataLoader:
    def __init__(self, cfg):
        self.cfg = cfg
        self.spatial = cfg["spatial"]
        self.frequency = cfg["frequency"]
        self.objS = spatialFilterClass(cfg)
        self.objF = frequencyFilterClass(cfg)
        

    def loadImage(self):
        if self.cfg["type"] == "image":
            imagePath = Image.open(self.cfg["path"]) #Loads Image
            imgResize = imagePath.resize((self.cfg["height"],self.cfg["width"])) #Resizes Image
            self.img = np.array(imgResize) #Converts to numpy array
            self.imgPadded = np.pad(self.img,((1,1),(1,1),(0,0)),'constant')    
        else:
            file = open(self.cfg["path"], "r")
            matrix = []
            for row in file:
                matrix.append([int(x) for x in row.split()])
            
            self.img = np.array(matrix)
            self.imgPadded = np.pad(self.img, [(1, 1), (1, 1)], mode='constant')
                 
         
    def save(self,ans):
        save_path = "outputs/result"
        if self.cfg["type"] == "image":
            
            im = Image.fromarray(ans)
            im.save(save_path+".jpg")
        else:
            f  = open(save_path, "w") 
            f.write(str(ans))
            f.close()
    
    def execute(self):
        self.loadImage()    
        if self.spatial:
            for i in self.spatial:
                if self.spatial[i] is True:
                    try:
                        method = getattr(self.objS,i)
                        ans = method(self.imgPadded)
                    except AttributeError:
                        ans = None

        if self.frequency:
            for i in self.frequency:
                if self.frequency[i] is True:
                    ans = self.objF.start(self.img,i)

        if ans is None:
            print("Incorrect Domain / Filter not found ")
        else:
            if self.cfg["save"]:
                self.save(ans)
            else:
                display(self.cfg["type"], ans)     
    

        
        

            
            



   