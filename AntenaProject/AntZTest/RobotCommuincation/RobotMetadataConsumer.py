

from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.ICD.telemetryMessage_pb2 import TelemetryMessage as TM
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.AntZTest.RobotCommuincation.ServerComm import ServerComm
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
class RobotMetadataConsumer(BaseAntsMetaDataConsumer):

    def __init__(self, config,server_comm:ServerComm):
        BaseAntsMetaDataConsumer.__init__(self, config)
        self.__server_comm=server_comm



    def ProcessPreRun(self,numberofsteps,maze,aditionaldata):
       pass

    def ProcessPreSysStep(self,step,worldimage:BaseTotalWorldImage, aditionaldata):
        pass

    def ProcessAntStep(self,step,ant:BasicAnt,antworldimage:BaseSingleAntWorldImage,move:AntStep,aditionaldata):
        robot_step=self.__GetRobotStep(ant,move)
        self.__server_comm.perform_step(ant_id=str(ant.ID),steps=robot_step)

    def __GetRobotStep(self,ant:BasicAnt,move:AntStep):
        robot_step=[]
        robot_step.append('s')
        current_position=ant.CurrentPosition
        next_position=move.Position
        #TODO fix this logic may be problematic-we are under the assumption of direction of axis and no walls- will fix in next version
        if(current_position.X!=next_position.X):
            if(current_position.X > next_position.X):
                robot_step.append('b1')
            if (current_position.Y < next_position.Y):
                robot_step.append('f1')

        if (current_position.Y != next_position.Y):
            if (current_position.Y > next_position.Y):
                robot_step.append('r')
                robot_step.append('f1')
            if (current_position.Y < next_position.Y):
                robot_step.append('l')
                robot_step.append('f1')
        return robot_step







    def ProcessPostSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        pass
    def ProcessPreStopRun(self,numberofsteps,worldimage:BaseTotalWorldImage , aditionaldata):
        pass