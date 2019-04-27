from abc import ABC,abstractmethod
class BaseTestStatusProvider(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def GetTestPerformanceData(self):
        #returns the additional data needed to get the full test performance
        #we will need to define what is common e.g peroformance (which we can standerize ) and what is unique
        pass
