from AntenaProject.TestingSuite.TestRunner.TestProcess.ICD.TestServiceStatus import TestServiceStatus
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
class TestController(object):
    def __init__(self,config:BaseConfigProvider,maze:MazeFacade):
        #build Test Process
        pass
    def Start(self):
        #Start Process
        pass
    def Finish(self):
        #Stop Process
        pass
    def ReportStatus(self)->list[TestServiceStatus]:
        #reports the status of all process
        pass

    @property
    def AreTestsFinished(self):
        return False
        pass