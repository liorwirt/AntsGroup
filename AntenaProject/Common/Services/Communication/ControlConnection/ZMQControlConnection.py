from AntenaProject.Common.Services.Communication.ControlConnection.BaseControlConncetion import BaseControlConnection

import zmq

class ZMQControlConnection(BaseControlConnection):
    def __init__(self,id,zmqcontrolport):
        self.__id=id
        BaseControlConnection.__init__(self,id)
        self.__zmqcontrolport=zmqcontrolport

    def _BuildConnection(self):
        context = zmq.Context()
        self.__socket = context.socket(zmq.PUB)
        self.__socket.bind("tcp://*:%s" % self.__zmqcontrolport)
    def _SendStatus(self,msg):
        self.__socket.send_pyobj(msg)


    def _CloseConnection(self):
       pass