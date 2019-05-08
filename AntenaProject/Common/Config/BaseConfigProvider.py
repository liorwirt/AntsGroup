from abc import ABC,abstractmethod

class BaseConfigProvider(ABC):
    @abstractmethod
    def GetConfigValueForSectionAndKey(self,section,key,defaultvalue=None):
        pass
    @abstractmethod
    def GetConfigSection(self,section,defaultvalue=None):
        pass