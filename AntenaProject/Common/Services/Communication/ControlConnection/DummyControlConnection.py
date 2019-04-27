from AntenaProject.Common.Services.Communication.ControlConnection.BaseControlConncetion import BaseControlConnection
class DummyControlConnection(BaseControlConnection):

    def _BuildConnection(self):
        pass
    def _SendStatus(self,msg):
        self.__socket.send_pyobj(msg)


    def _CloseConnection(self):
       pass