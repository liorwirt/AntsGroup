

import json
from AntenaProject.Common.Services.Communication.ControlConnection.ICD.Enums import ServiceStatusEnum






class StatusMessege(object):
    def __init__(self,id,status=ServiceStatusEnum.Stopped,exception={}):
        self.__id=id
        self.__Status=status
        self.__ExceptionDict=exception

    def SetException(self, ex):
        self.__ExceptionDict = self.__exception_as_dict(ex)
        self.__Status=ServiceStatusEnum.Error
    def __str__(self):
        return format(f"status for id ={self.__id} status={self.__Status} exception-{self.__ExceptionDict}")

    @property
    def Status(self):
        return self.__Status

    @Status.setter
    def Status(self, status):
        self.__Status=status

    @property
    def ID(self):
        return self.__id

    @property
    def ExceptionDict(self):
        return self.__ExceptionDict

    @staticmethod
    def GetStatusMessegeFromJson(jsonStr):
        datadict = json.loads(jsonStr)
        return StatusMessege(id=int(datadict['ID']),status=ServiceStatusEnum(int(datadict['Status'])),exception= dict(datadict['ExceptionDict']))

    @property
    def Dict_Representation(self):
        datadict={}
        datadict['ID']=self.__id
        datadict['ExceptionDict']=self.__ExceptionDict
        datadict['Status'] =self.__Status.value
        return json.dumps(datadict)

    def __exception_as_dict(self,ex):
        return dict(type=ex.__class__.__name__,
                    errno=ex.errno, message=ex.message,
                    strerror=self.exception_as_dict(ex.strerror)
                    if isinstance(ex.strerror,Exception) else ex.strerror)


