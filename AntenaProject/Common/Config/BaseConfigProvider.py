from abc import ABC,abstractmethod

class BaseConfigProvider(ABC):
    @abstractmethod
    def GetConfigValuesForKey(self,key,defaultvalue=None):
        pass