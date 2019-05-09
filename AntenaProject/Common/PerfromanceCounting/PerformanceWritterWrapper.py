from AntenaProject.Common.PerfromanceCounting.BasePerofromanceWriter import BasePerofromanceWriter
from AntenaProject.Common.PerfromanceCounting.LoggerPerofromanceWriter import LoggerPerofromanceWriter
import logging
class PerofromanceWriterWrapper(BasePerofromanceWriter):
    def __init__(self):
        #TODO add DILL Serialization
        #TODO add Messege to web
        self.__Writers=[LoggerPerofromanceWriter]
    def  WritePerformance(self,name,performanceTime):
        for writer in self.__Writers:
            writer.WritePerformance(writer,name,performanceTime)