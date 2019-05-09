from AntenaProject.Common.PerfromanceCounting.BasePerofromanceWriter import BasePerofromanceWriter
from AntenaProject.Common.PerfromanceCounting.LoggerPerofromanceWriter import LoggerPerofromanceWriter
import logging
class PerofromanceWriterWrapper(BasePerofromanceWriter):
    def __init__(self,config):
        #TODO add Messege to web
        BasePerofromanceWriter.__init__(self,config)
        self.__Writers=[]

    def AddWritter(self,writter:BasePerofromanceWriter):
        self.__Writers.append(writter)
    def  WritePerformance(self,name,performanceTime):
        for writer in self.__Writers:
            writer.WritePerformance(name,performanceTime)