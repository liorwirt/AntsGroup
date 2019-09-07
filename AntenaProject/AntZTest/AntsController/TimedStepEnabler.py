from AntenaProject.AntZTest.AntsController.BaseStepEnabler import BaseStepEnabler
from time import time
class TimedStepEnabler(BaseStepEnabler):
    def __init__(self,seconds_to_halt):
        self.__seconds_to_halt=seconds_to_halt
        self.__last_step_time=time()
    def ShouldPerformStep(self) -> bool:
        passed_time=int(time()-self.__last_step_time)
        if passed_time>self.__seconds_to_halt:
            self.__last_step_time=time()
            return True
        return False