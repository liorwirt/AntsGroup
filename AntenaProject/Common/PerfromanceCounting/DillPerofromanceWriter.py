from AntenaProject.Common.PerfromanceCounting.BasePerofromanceWriter import BasePerofromanceWriter
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
import dill
import os
class DillPerofromanceWriter(BasePerofromanceWriter):
    def __init__(self,config:BaseConfigProvider,folder):
        BasePerofromanceWriter.__init__(self,config)
        self.__filename=os.path.join(folder,"Performance.dill")

    def  WritePerformance(self,name,performanceTime):
        with open(self.__filename, "ab") as dill_file:
            dill.dump(performanceTime, dill_file)

