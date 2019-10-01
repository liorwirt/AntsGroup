from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from typing import List
import time
import numpy as np

class SimpleSingleAntWorldImage(BaseSingleAntWorldImage):
    def __init__(self, worldImage: np.array,ants,visible_nodes=np.array):
        self.__WorldImage = worldImage
        self.__visible_nodes=visible_nodes
        self.__Ants = ants
        self.__AntUpdateTimes = SimpleSingleAntWorldImage.__create_ant_update_times_list(ants)

    @property
    def VisibleNodes(self):
        # TODO turn this to a list (np.where, etc)
        return self.__visible_nodes

    @property
    def WorldImage(self):
        return self.__WorldImage

    def Ants(self):
        return self.__Ants

    @staticmethod
    def __create_ant_update_times_list(ants):
        now = time.time()
        ret_list = []
        for _ in ants:
            ret_list.append(now)

        return ret_list
