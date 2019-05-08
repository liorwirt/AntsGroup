from AntenaProject.Common.PerfromanceCounting.BasePerofromanceWriter import BasePerofromanceWriter
import logging
class LoggerPerofromanceWriter(BasePerofromanceWriter):
    def  WritePerformance(self,name,performanceTime):
        logging.info(format(f"Step {name} took {performanceTime}"))