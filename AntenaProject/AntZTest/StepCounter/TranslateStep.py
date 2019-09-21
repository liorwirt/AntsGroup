from AntenaProject.AntZTest.StepCounter.Enums import DirectionsEnum
from AntenaProject.AntZTest.StepCounter.Enums import StepEnum
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from typing import List
from AntenaProject.AntZTest.StepCounter.AntStepProcesser import AntStepProcesser
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep

'''assumes start position from config,single step only (i.e max in tur in direction change and movement of one cell north is up right is plus
diagonal movement not supported!'''
class TranslateStep(object):
    def __init__(self, config, ant_step_processor: AntStepProcesser):
        self.__ant_step_processor = ant_step_processor
        self._config=config
        self.__initial_direction = self.__initial_direction = (DirectionsEnum)((int)(self._config.GetConfigValueForSectionAndKey('InitialPosition', 'InitialDirection', 1)))

        self.__initial_position_x = (int)(
            self._config.GetConfigValueForSectionAndKey('InitialPosition', 'InitialPosition_x', 1))
        self.__initial_position_y = (int)(
            self._config.GetConfigValueForSectionAndKey('InitialPosition', 'InitialPosition_y', 1))



    def TranlateStep(self, step: AntStep) -> List[StepEnum]:
        ant_direction = self.__initial_direction
        ant_position_x = self.__initial_position_x
        ant_position_y = self.__initial_position_y
        if (self.__ant_step_processor.is_ant_on_field(step.AntId)):
            current_position = self.__ant_step_processor.get_ant_position_and_direction(step.AntId)
            ant_direction = current_position[2]
            ant_position_y = current_position[1]
            ant_position_x = current_position[0]

        x_axis_movement = self.__get_x_axis_movement(ant_position_x, step.Position.X,ant_direction)
        y_axis_movement = self.__get_y_axis_movement(ant_position_y, step.Position.Y,ant_direction)
        return  x_axis_movement+y_axis_movement


    def __get_x_axis_movement(self, original_position_x, new_step_position_x,original_ant_direction:DirectionsEnum)->List[StepEnum]:
        movements = []
        diff_x = original_position_x - new_step_position_x
        if diff_x == 0:
            return movements
        #car direction on X axis
        if (original_ant_direction==DirectionsEnum.East):
            if(diff_x<0):
                movements.append(StepEnum.Forward)
            else:
                movements.append(StepEnum.Back)

        if (original_ant_direction == DirectionsEnum.West):
            if (diff_x < 0):
                movements.append(StepEnum.Back)
            else:
                movements.append(StepEnum.Forward)

        # car direction on Y axis
        if (original_ant_direction == DirectionsEnum.North):
            if (diff_x < 0):
                movements.append(StepEnum.TurnRight)
                movements.append(StepEnum.Forward)
            else:
                movements.append(StepEnum.TurnLeft)
                movements.append(StepEnum.Forward)

        if (original_ant_direction == DirectionsEnum.South):
            if (diff_x < 0):
                movements.append(StepEnum.TurnLeft)
                movements.append(StepEnum.Forward)
            else:
                movements.append(StepEnum.TurnRight)
                movements.append(StepEnum.Forward)

        return movements




    def __get_y_axis_movement(self, original_position_y, new_step_position_y,original_ant_direction:DirectionsEnum):
        movements = []
        diff_y = original_position_y - new_step_position_y
        if diff_y == 0:
            return movements
        # car direction on X axis
        if (original_ant_direction == DirectionsEnum.East):
            if (diff_y < 0):
                movements.append(StepEnum.TurnRight)
                movements.append(StepEnum.Forward)
            else:
                movements.append(StepEnum.TurnLeft)
                movements.append(StepEnum.Forward)

        if (original_ant_direction == DirectionsEnum.West):
            if (diff_y < 0):
                movements.append(StepEnum.TurnLeft)
                movements.append(StepEnum.Forward)
            else:
                movements.append(StepEnum.TurnRight)
                movements.append(StepEnum.Forward)

        # car direction on Y axis
        if (original_ant_direction == DirectionsEnum.North):
            if (diff_y < 0):
                movements.append(StepEnum.Back)

            else:

                movements.append(StepEnum.Forward)

        if (original_ant_direction == DirectionsEnum.South):
            if (diff_y < 0):
                movements.append(StepEnum.Forward)
            else:
                movements.append(StepEnum.Back)

        return movements
