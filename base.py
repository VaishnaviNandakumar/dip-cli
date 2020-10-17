import numpy as np
import yaml
from PIL import Image
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import stats


def splitChannels(mat, h, w):
        redChannel, greenChannel, blueChannel = [] , [] , []
        for i in range(h):
            l1, l2, l3 = [] , [] , []
            for j in range(w):
                r,g,b = mat[i][j][0], mat[i][j][1], mat[i][j][2]
                
                l1.append(r)
                l2.append(g)
                l3.append(b)

            redChannel.append(l1)
            greenChannel.append(l2)
            blueChannel.append(l3)
        return redChannel, greenChannel, blueChannel