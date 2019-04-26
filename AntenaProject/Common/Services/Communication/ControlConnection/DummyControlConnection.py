from AntenaProject.Common.Services.Communication.ControlConnection.BaseControlConncetion import BaseControlConnection
class DummyControlConnection(BaseControlConnection):
    def __SendStatus(self):
        print(format(f'reporting dummy data - {self.__repr__()}'))