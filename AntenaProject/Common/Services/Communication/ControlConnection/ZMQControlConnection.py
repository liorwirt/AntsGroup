from AntenaProject.Common.Services.Communication.ControlConnection.BaseControlConncetion import BaseControlConnection

import zmq

class ZMQControlConnection(BaseControlConnection):
    def __init__(self,id,zmqcontrolport):
        self.__id=id
        BaseControlConnection.__init__(self,id)
        self.__zmqcontrolport=zmqcontrolport

    def _BuildConnection(self):
        context = zmq.Context()
        self.__socket = context.socket(zmq.REQ)
        self.__socket.connect("tcp://localhost:%s" % self.__zmqcontrolport)
    def _SendStatus(self,jsonDict):
        self.__socket.send_json(jsonDict)
        self.__socket.recv()
        j=9


    def _CloseConnection(self):
       pass