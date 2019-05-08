from contextlib import ContextDecorator
from time import time
from AntenaProject.Common.PerfromanceCounting.BasePerofromanceWriter import BasePerofromanceWriter
class PerformanceCounter(ContextDecorator):
    def __init__(self, name,performanceWriter:BasePerofromanceWriter):
        self.__Name = name
        self.__performancewriter = performanceWriter

    def __enter__(self):
        self._startTime=time()

    def __exit__(self, exc_type, exc, exc_tb):
       totaltime=time()-self._startTime
       self.__performancewriter.WritePerformance(self.__Name,totaltime)