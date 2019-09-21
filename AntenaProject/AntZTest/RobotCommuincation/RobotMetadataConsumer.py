from AntenaProject.AntZTest.StepCounter.Enums import DirectionsEnum
from AntenaProject.AntZTest.StepCounter.Enums import StepEnum
from AntenaProject.AntZTest.StepCounter.RobotAntPosition import RobotAntPosition
from AntenaProject.AntZTest.StepCounter.AntStepProcesser import AntStepProcesser
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.AntZTest.StepCounter.TranslateStep import TranslateStep

from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.ICD.telemetryMessage_pb2 import TelemetryMessage as TM
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.AntZTest.RobotCommuincation.ServerComm import ServerComm
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
import logging
class RobotMetadataConsumer(BaseAntsMetaDataConsumer):

    def __init__(self, config,server_comm:ServerComm,ants_step_processor:AntStepProcesser):
        BaseAntsMetaDataConsumer.__init__(self, config)
        self.__server_comm=server_comm
        self._ants_step_processor=ants_step_processor
        self.__ants_step_transelator=TranslateStep(config,ants_step_processor)

        self._movement_translation = {}
        self._movement_translation[StepEnum.Forward] = 'f1'
        self._movement_translation[StepEnum.Back] = 'b1'
        self._movement_translation[StepEnum.TurnLeft] = 'l'
        self._movement_translation[StepEnum.TurnRight] = 'r'
        self._movement_translation[StepEnum.NoStep]='s'


    def ProcessPreRun(self,numberofsteps,maze,aditionaldata):
       pass

    def ProcessPreSysStep(self,step,worldimage:BaseTotalWorldImage, aditionaldata):
        pass

    def ProcessAntStep(self,step,ant:BasicAnt,antworldimage:BaseSingleAntWorldImage,move:AntStep,aditionaldata):
        movements=self.__ants_step_transelator.TranlateStep(move)
        for movement in movements:
            robot_step=self._movement_translation[movement]
            logging.info(format(
                f"Sending to ant {ant.ID} step {robot_step} "))
            command_processed=self.__server_comm.perform_step(ant_id=str(ant.ID), step=robot_step)
            if not command_processed:
                logging.error(format(
                    f"Command to ant {ant.ID} step {robot_step} was not acked!!!! "))
                #TODO-what to do now?
            else:
                logging.info(format(
                    f"Command to ant {ant.ID} step {robot_step} was  acked  "))
                self._ants_step_processor.process_ant_step(ant_id=ant.ID,step=movement)



    def ProcessPostSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        pass
    def ProcessPreStopRun(self,numberofsteps,worldimage:BaseTotalWorldImage , aditionaldata):
        pass