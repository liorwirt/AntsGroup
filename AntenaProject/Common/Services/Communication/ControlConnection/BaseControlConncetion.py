from abc import ABC, abstractmethod
import threading
import time
import sys
from AntenaProject.Common.Services.Communication.ControlConnection.ICD.StatusMessege import StatusMessege
lock = threading.Lock()
BrodcastCondition=False
class BaseControlConnection(ABC):


    def __init__(self,id):
        self.__StatusMessege=StatusMessege(id)
        self.__BrodacastThread=None
        sys.excepthook = self.except_hook

    def Start(self):
        global BrodcastCondition
        if  self.__BrodacastThread is None:
            with lock:

                BrodcastCondition=True
                self.__BrodacastThread = threading.Thread(target=self.__BrodacastThreadFunction,args=[self.__StatusMessege])

                self.__BrodacastThread.start()

    def Stop(self):
        global BrodcastCondition
        if self.__BrodacastThread is not None:
            with lock:
                BrodcastCondition = False

    def except_hook(self,exctype, value, traceback):
        self.__StatusMessege.SetException(exc_info=(exctype, value, traceback))

    def __BrodacastThreadFunction(self,statusmessege):

        global BrodcastCondition
        self._BuildConnection()
        while True:
            time.sleep(1)
            with lock:
                if BrodcastCondition == True:
                    self._SendStatus(statusmessege.Dict_Representation)
                else:
                    self._CloseConnection()
                    break

    def ReportStatus(self,status):
        with lock:
            self.__StatusMessege.Status=status
    def ReportException(self, ex):
        with lock:
            self.__StatusMessege.SetException(ex)


    @abstractmethod
    def _SendStatus(self,statusmessege):
        pass
    @abstractmethod
    def _BuildConnection(self):
        pass
    @abstractmethod
    def _CloseConnection(self):
        pass