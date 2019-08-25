from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.ICD.telemetryMessage_pb2 import TelemetryMessage as TM
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum,AntType
import socket
from AntenaProject.AntZTest.AntsMetaDataConsumer.MetaDataToNodeStateInterperter import MetaDataToNodeStateInterperter


class MetrySenderMetaDataConsumer(BaseAntsMetaDataConsumer):

    def __init__(self, config, interperter: MetaDataToNodeStateInterperter):
        BaseAntsMetaDataConsumer.__init__(self, config)
        self.__interperter = interperter
        self._Port = int(config.GetConfigValueForSectionAndKey('MulitCastDefinations', 'Port'))
        self._MulticastAddr = config.GetConfigValueForSectionAndKey('MulitCastDefinations', 'IP')
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self._socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)

        self._NodeStateToStr = {}
        self._NodeStateToStr[NodeStateEnum.Ant] = 'open'
        self._NodeStateToStr[NodeStateEnum.Obs] = 'wall'
        self._NodeStateToStr[NodeStateEnum.UnExplored] = 'open'
        self._NodeStateToStr[NodeStateEnum.Clear] = 'open'
        self._ScoutAntType = 'scout'
        self._TransAntType = 'trans'

    def ProcessPreRun(self, numberofsteps, maze, aditionaldata):
        pass

    def ProcessPreSysStep(self, step, worldimage: BaseTotalWorldImage, aditionaldata):
        pass

    def ProcessAntStep(self, step, ant: BasicAnt, antworldimage: BaseSingleAntWorldImage, move, aditionaldata):
        if (ant.ID == 0):
            return
        if (ant.CurrentPosition.X == 0):
            return
        if (ant.CurrentPosition.Y == 0):
            return

        msg = TM()
        msg.id = int(ant.ID)
        msg.battery = int(100)
        msg.x = ant.CurrentPosition.X
        msg.y = ant.CurrentPosition.Y
        msg.angle = int(0)
        pos_ll = Position(ant.CurrentPosition.X - 1, ant.CurrentPosition.Y)
        pos_ul = Position(ant.CurrentPosition.X, ant.CurrentPosition.Y - 1)
        pos_rl = Position(ant.CurrentPosition.X + 1, ant.CurrentPosition.Y)
        pos_bl = Position(ant.CurrentPosition.X, ant.CurrentPosition.Y + 1)
        msg.ul = 'open'
        msg.ll = 'open'
        msg.rl = 'open'
        msg.bl = 'open'

        if ant.Type() == AntType.Transmission:
            msg.type = self._TransAntType
        else:
            msg.type = self._ScoutAntType

        for node in self.__interperter.Interpert(antworldimage.VisibleNodes):
            if (node.Position == pos_ll):
                msg.ll = self._GetNodeStr(node.NodeState)
            if (node.Position == pos_ul):
                msg.ul = self._GetNodeStr(node.NodeState)
            if (node.Position == pos_rl):
                msg.rl = self._GetNodeStr(node.NodeState)
            if (node.Position == pos_bl):
                msg.bl = self._GetNodeStr(node.NodeState)

        serialized = msg.SerializeToString(msg)

        # Create a socket (SOCK_STREAM means a TCP socket)

        self._socket.sendto(serialized, (self._MulticastAddr, self._Port))

    def _GetNodeStr(self, nodestate: NodeStateEnum):
        return self._NodeStateToStr[nodestate]

    def ProcessPostSysStep(self, step, worldimage: BaseTotalWorldImage, aditionaldata):
        pass

    def ProcessPreStopRun(self, numberofsteps, worldimage: BaseTotalWorldImage, aditionaldata):
        pass
