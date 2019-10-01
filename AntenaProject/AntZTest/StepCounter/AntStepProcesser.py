from AntenaProject.AntZTest.StepCounter.Enums import DirectionsEnum
from AntenaProject.AntZTest.StepCounter.Enums import StepEnum
from AntenaProject.AntZTest.StepCounter.RobotAntPosition import RobotAntPosition
from AntenaProject.Common.AntsBasicStructures.Position import Position
class AntStepProcesser(object):
    #Top Left corner is our start
    #North is up
    def __init__(self,config):
        self._config = config

        self.__initial_direction = (DirectionsEnum)((int)(self._config.GetConfigValueForSectionAndKey('InitialPosition', 'InitialDirection', 1)))
        self.__initial_position_x = (int)(
            self._config.GetConfigValueForSectionAndKey('InitialPosition', 'InitialPosition_x', 1))
        self.__initial_position_y = (int)(
            self._config.GetConfigValueForSectionAndKey('InitialPosition', 'InitialPosition_y', 1))
        self._positions={}
        self._next_turn_left_direction={}
        self._next_turn_left_direction[DirectionsEnum.North]=DirectionsEnum.West
        self._next_turn_left_direction[DirectionsEnum.West] = DirectionsEnum.South
        self._next_turn_left_direction[DirectionsEnum.South] = DirectionsEnum.East
        self._next_turn_left_direction[DirectionsEnum.East] = DirectionsEnum.North

        self._next_turn_right_direction = {}
        self._next_turn_right_direction[DirectionsEnum.North] = DirectionsEnum.East
        self._next_turn_right_direction[DirectionsEnum.East] = DirectionsEnum.South
        self._next_turn_right_direction[DirectionsEnum.South] = DirectionsEnum.West
        self._next_turn_right_direction[DirectionsEnum.West] = DirectionsEnum.North


    def process_ant_step(self,ant_id,step:StepEnum):
        #create ant and init it!
        if(ant_id not in self._positions):
            self._positions[ant_id]=RobotAntPosition(direction= self.__initial_direction,X= self.__initial_position_x,Y= self.__initial_position_y)
        if(step==StepEnum.NoStep):
            return
        self._update_ant_position(ant_id,step)
        self._update_ant_direction(ant_id, step)

    def is_ant_on_field(self,ant_id):
        return ant_id  in self._positions
    def initial_position(self)->Position:
        return Position(x=self.__initial_position_x,y=self.__initial_position_y)
    def get_ant_position_and_direction(self,ant_id):
        #create ant and init it!
        if(ant_id not in self._positions):
           return (-1,-1,-1)
        return (self._positions[ant_id].X,self._positions[ant_id].Y,self._positions[ant_id].direction)

    def _update_ant_position(self,ant_id,step:StepEnum):

        if (self._positions[ant_id].direction == DirectionsEnum.East and step==StepEnum.Forward):
            self._positions[ant_id].X = self._positions[ant_id].X + 1
        if (self._positions[ant_id].direction == DirectionsEnum.East and step==StepEnum.Back):
            self._positions[ant_id].X = self._positions[ant_id].X - 1

        if (self._positions[ant_id].direction == DirectionsEnum.West and step == StepEnum.Back):
            self._positions[ant_id].X = self._positions[ant_id].X + 1
        if (self._positions[ant_id].direction == DirectionsEnum.West and step == StepEnum.Forward):
            self._positions[ant_id].X = self._positions[ant_id].X - 1

        if (self._positions[ant_id].direction == DirectionsEnum.South and step == StepEnum.Forward):
            self._positions[ant_id].Y = self._positions[ant_id].Y + 1
        if (self._positions[ant_id].direction == DirectionsEnum.South and step == StepEnum.Back):
            self._positions[ant_id].Y = self._positions[ant_id].Y - 1

        if (self._positions[ant_id].direction == DirectionsEnum.North and step == StepEnum.Back):
            self._positions[ant_id].Y = self._positions[ant_id].Y+ 1
        if (self._positions[ant_id].direction == DirectionsEnum.North and step == StepEnum.Forward):
            self._positions[ant_id].Y = self._positions[ant_id].Y - 1


    def _update_ant_direction(self, ant_id, step: StepEnum):
        if (step == StepEnum.TurnLeft):
            self._positions[ant_id].direction = self._next_turn_left_direction[self._positions[ant_id].direction]
        if (step == StepEnum.TurnRight):
            self._positions[ant_id].direction = self._next_turn_right_direction[self._positions[ant_id].direction]

