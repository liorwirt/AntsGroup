from abc import ABC,abstractmethod
class BaseStepEnabler(ABC):
    @property
    @abstractmethod
    def ShouldPerformStep(self)->bool:
        pass