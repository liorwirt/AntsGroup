from abc import ABC,abstractmethod
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
class BasePerofromanceWriter(ABC):
    def __init__(self,config:BaseConfigProvider):
        self._config=config
    @abstractmethod
    def WritePerformance(self,name,performanceTime):
        pass