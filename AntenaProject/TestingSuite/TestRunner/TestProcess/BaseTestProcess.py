from AntenaProject.Common.Services.BaseService import BaseService
from AntenaProject.TestingSuite.TestRunner.TestProcess.BaseTestStatusProvider import BaseTestStatusProvider
class BaseTestProcess(BaseService):
    def __init__(self,id,**kwargs):
        #Create Test
        self.__TestStatusProvider=self.GetStatusProvider()
        pass
    def GetStatusProvider(self)->BaseTestStatusProvider:
        #get the status provider
        pass
    def UpdateData(self):
        #update data to be send to TestController
        pass
    def CleanUP(self):
        #cleanup after run
        pass
