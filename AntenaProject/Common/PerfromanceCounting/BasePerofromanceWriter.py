from abc import ABC,abstractmethod

class BasePerofromanceWriter(ABC):
    @abstractmethod
    def WritePerformance(self,name,performanceTime):
        pass