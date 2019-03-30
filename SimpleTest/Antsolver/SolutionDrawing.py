import numpy as np
import matplotlib.pyplot as plt

class SolutionDrawing(object):
    def __init__(self,initialnode,finalnode,occupancy_map):
        self.initial_node=initialnode
        self.final_node=finalnode
        self.occupancy_map=occupancy_map

    def __represent_map(self):
        ''' Represents the map '''
        # Map representation
        plt.plot(self.initial_node[1],self.initial_node[0], 'ro', markersize=10)
        plt.plot(self.final_node[1],self.final_node[0], 'bo', markersize=10)
        plt.imshow(self.occupancy_map, cmap='gray', interpolation = 'nearest')
        plt.show()
        plt.close()


    def __represent_path(self, path,pathcolor):
        ''' Represents the path in the map '''
        x = []
        y = []
        for p in path:
            x.append(p[1])
            y.append(p[0])
        plt.plot(x,y,color=pathcolor)

    def DrawPaths(self,acoPath,optimalpath):
        if(acoPath is not None):
            self.__represent_path(acoPath,"blue")
        if (acoPath is not optimalpath):
            self.__represent_path(optimalpath,"orange")
        self.__represent_map()