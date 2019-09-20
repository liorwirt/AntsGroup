from AntenaProject.AntZTest.StepCounter.Enums import DirectionsEnum
from AntenaProject.AntZTest.StepCounter.Enums import StepEnum
from AntenaProject.AntZTest.StepCounter.RovbotAntPosition import RobotAntPosition
class AntStepProcesser(object):
    #Top Left corner is our start
    #North is up
    def __init__(self,config):
        self._config = config
        self.__initial_direction = (DirectionsEnum)(self._config.GetConfigValueForSectionAndKey('InitialPosition', 'InitialDirection', 1))
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

    def process_ant_step(self,antid,step:StepEnum):
        #create ant and init it!
        if(antid not in self._positions):
            self._positions[antid]=RobotAntPosition(direction= self.__initial_direction,X= self.__initial_position_x,Y= self.__initial_position_y)
        if(step==StepEnum.NoStep):
            return
        self._update_ant_position(antid,step)
        self._update_ant_direction(antid, step)

    def get_ant_position_and_direction(self,antid):
        #create ant and init it!
        if(antid not in self._positions):
           return (-1,-1,-1)
        return (self._positions[antid].X,self._positions[antid].Y,self._positions[antid].direction)

    def _update_ant_position(self,antid,step:StepEnum):

        if (self._positions[antid].direction == DirectionsEnum.East and step==StepEnum.Forward):
            self._positions[antid].X = self._positions[antid].X + 1
        if (self._positions[antid].direction == DirectionsEnum.East and step==StepEnum.Back):
            self._positions[antid].X = self._positions[antid].X - 1

        if (self._positions[antid].direction == DirectionsEnum.West and step == StepEnum.Back):
            self._positions[antid].X = self._positions[antid].X + 1
        if (self._positions[antid].direction == DirectionsEnum.West and step == StepEnum.Forward):
            self._positions[antid].X = self._positions[antid].X - 1

        if (self._positions[antid].direction == DirectionsEnum.South and step == StepEnum.Forward):
            self._positions[antid].Y = self._positions[antid].Y + 1
        if (self._positions[antid].direction == DirectionsEnum.South and step == StepEnum.Back):
            self._positions[antid].Y = self._positions[antid].Y - 1

        if (self._positions[antid].direction == DirectionsEnum.North and step == StepEnum.Back):
            self._positions[antid].Y = self._positions[antid].Y+ 1
        if (self._positions[antid].direction == DirectionsEnum.North and step == StepEnum.Forward):
            self._positions[antid].Y = self._positions[antid].Y - 1


    def _update_ant_direction(self, antid, step: StepEnum):
        if (step == StepEnum.TurnLeft):
            self._positions[antid].direction = self._next_turn_left_direction[self._positions[antid].direction]
        if (step == StepEnum.TurnRight):
            self._positions[antid].direction = self._next_turn_right_direction[self._positions[antid].direction]

