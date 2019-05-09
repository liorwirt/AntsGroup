from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
import logging
from pprint import pformat
class LoggingAntsMetaDataConsumer(BaseAntsMetaDataConsumer):


    def ProcessPreRun(self,numberofsteps,maze,aditionaldata):
        logging.info(format(f"pre run on maze {maze.Name} for {numberofsteps} steps aditionaldata:{pformat(aditionaldata)}"))


    def ProcessPreSysStep(self,step,worldimage:BaseTotalWorldImage, aditionaldata):
        logging.info(format(f"Process PreSys Step {step}  coverage {worldimage.Coverage} aditionaldata:{pformat(aditionaldata)}"))

    def ProcessAntStep(self,step,ant:BasicAnt,antworldimage,move,aditionaldata):
        logging.info(format(f"Process Ant Step {step}  ant {ant.ID} moves to {move} from position{ant.CurrentPosition} aditionaldata:{pformat(aditionaldata)}"))

    def ProcessPostSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        logging.info(format(f"Process PostSys Step {step}  coverage {worldimage.Coverage} aditionaldata:{pformat(aditionaldata)}"))

    def ProcessPreStopRun(self,numberofsteps,worldimage:BaseTotalWorldImage , aditionaldata):
        logging.info(format(f"pre end run on maze coverage {worldimage.Coverage} for {numberofsteps} steps aditionaldata:{pformat(aditionaldata)}"))
