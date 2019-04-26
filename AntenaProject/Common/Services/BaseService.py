from abc import ABC, abstractmethod

import sys
from AntenaProject.Common.Services.Communication.ConnectionBuilder import ConnectionBuilder


class BaseService(ABC):
    def __init__(self,id,**kwargs):
        self.__id=id
        self.__Connection=None
        sys.excepthook = self.except_hook
        self.__Connection=ConnectionBuilder.CreateControlConnection(id,kwargs)
        self._InnerInit(kwargs)
        self.__Connection.Start()

    def except_hook(self,exctype, value, traceback):
        if self.__Connection is not None:
            self.__Connection.ReportException( exc_info=(exctype, value, traceback))
        self._InnerExceptionHandeling(exctype, value, traceback)

    def SetStatus(self,status):
        self.__Connection.ReportStatus(status)


    @abstractmethod
    def _InnerInit(self,kwargs):
        pass

    @abstractmethod
    def _InnerExceptionHandeling(self,exctype, value, traceback):
        pass





