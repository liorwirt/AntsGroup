from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from typing import List
import time


class SimpleSingleAntWorldImage(BaseSingleAntWorldImage):
    def __init__(self, visiblenodes, ants):
        self.__VisibleNodes = visiblenodes
        self.__Ants = SimpleSingleAntWorldImage.__create_ant_list_with_update_times(ants)

    @property
    def VisibleNodes(self):
        return self.__VisibleNodes

    def Ants(self):
        return self.__Ants

    @staticmethod
    def __create_ant_list_with_update_times(ants):
        now = time.time()
        ret_list = []
        for ant in ants:
            ret_list.append((ant, now))

        return ret_list
