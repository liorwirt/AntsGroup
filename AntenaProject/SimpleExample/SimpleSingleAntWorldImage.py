from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from typing import List
import time
import numpy as np

class SimpleSingleAntWorldImage(BaseSingleAntWorldImage):
    def __init__(self, worldImage: np.array, ants):
        self.__WorldImage = worldImage
        self.__Ants = SimpleSingleAntWorldImage.__create_ant_list_with_update_times(ants)

    @property
    def VisibleNodes(self):
        # TODO turn this to a list (np.where, etc)
        return self.__WorldImage

    @property
    def WorldImage(self):
        return self.__WorldImage

    def Ants(self):
        return self.__Ants

    @staticmethod
    def __create_ant_list_with_update_times(ants):
        now = time.time()
        ret_list = []
        for ant in ants:
            ret_list.append((ant, now))

        return ret_list
