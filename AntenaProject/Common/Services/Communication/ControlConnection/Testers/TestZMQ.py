from AntenaProject.Common.Services.BaseService import BaseService
from AntenaProject.Common.Services.Communication.ControlConnection.ICD.Enums import ServiceStatusEnum
from AntenaProject.Common.Services.Communication.ControlConnection.ICD.StatusMessege import StatusMessege
import zmq
import numpy as np

class TesterService(BaseService):
    def __init__(self,**kwargs):
        BaseService.__init__(self,**kwargs)
    def _InnerInit(self,kwargs):
        pass
    def _InnerExceptionHandeling(self,exctype, value, traceback):
        pass



if __name__ == '__main__':
    port=5556
    service1=TesterService(id=1,commtype="zmq",zmqcontrolport=port)
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:%s" % port)
    while True:
        message = socket.recv_json()
        print(f"Received: {StatusMessege.GetStatusMessegeFromJson(message)}")
        ok='ok'
        #TODO add json Ack
        socket.send(ok.encode('utf-8'))
        # just test state code
        service1.SetStatus(ServiceStatusEnum(np.random.random_integers(1, 5)))
