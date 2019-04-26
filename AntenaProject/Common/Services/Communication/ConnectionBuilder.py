from AntenaProject.Common.Services.Communication.ControlConnection.BaseControlConncetion import BaseControlConnection
from AntenaProject.Common.Services.Communication.ControlConnection.DummyControlConnection import DummyControlConnection
from AntenaProject.Common.Services.Communication.ControlConnection.ZMQControlConnection import ZMQControlConnection
import traceback
class ConnectionBuilder(object):
    #TODO LOGGGGGGG
    @staticmethod
    def CreateControlConnection(id,args):
        _id=int(id)
        if ('commtype' not in args.keys()):
            return DummyControlConnection(_id)

        if(args['commtype'].lower()=='dummy'):
            return DummyControlConnection(_id)

        if(args['commtype'].lower()=='zmq'):
            if ('zmqcontrolport' in args.keys()):
                try:
                    connection= ZMQControlConnection(_id,int(args['zmqcontrolport']))
                    return connection
                except Exception:
                    traceback.print_exc()
            else:
                raise ValueError(format(f'requested ZMQ control channel but no port was given'))
