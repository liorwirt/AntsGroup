from AntenaProject.Common.AntsBasicStructures.Enums import AlgCommandEnum
from AntenaProject.Common.AntsBasicStructures.AlgExternalCommand import AlgExternalCommand
from AntenaProject.Common.AntsBasicStructures.Position import Position
import struct
from AntenaProject.ICD.uiCommand_pb2 import UiCommandMessage as CM
import socket
import concurrent.futures
import queue
import threading

class CommandsReciver(object):

    def __init__(self, config, ):
        self._Port = int(config.GetConfigValueForSectionAndKey('MulitCastDefinations', 'CommandPort'))
        self._MulticastAddr = config.GetConfigValueForSectionAndKey('MulitCastDefinations', 'CommandIP')

        server_address = ('', self._Port)

        # Create the socket
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind to the server address
        self._socket.bind(server_address)

        group = socket.inet_aton(self._MulticastAddr)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self._socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        self.__pipeline = queue.Queue(maxsize=10)
        self.__event = threading.Event()

    def Start(self):
        self.__Thread = threading.Thread(target=self.Listner, args=(self._socket,self.__pipeline,self.__event))
        self.__Thread .start()

    def Stop(self):
        self.__event.set()
        self.__Thread.join()
        self._socket.close()
    def GetCommands(self):
        commands=[]
        while not self.__pipeline.empty():
            command=self.__pipeline.get_nowait()
            commands.append(command)

        return commands

    def Listner(self,socket,queue, event):
        Commands = {}
        Commands['MarkNotRelevant'] = AlgCommandEnum.NotRelevent
        Commands['MarkClear'] = AlgCommandEnum.Clear
        Commands['MarkBlocked'] = AlgCommandEnum.Blocked
        Commands['MarkPriority'] = AlgCommandEnum.Priority
        while not event.is_set():
            data = socket.recv(1024)
            msg = CM()
            msg.ParseFromString(data)
            command=AlgExternalCommand(position=Position(msg.x, msg.y), command=Commands[msg.action])
            queue.put(command)

