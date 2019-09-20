from unittest import TestCase
from AntenaProject.AntZTest.StepCounter.Enums import DirectionsEnum
from AntenaProject.AntZTest.StepCounter.Enums import StepEnum
from AntenaProject.AntZTest.StepCounter.RovbotAntPosition import RobotAntPosition
from AntenaProject.AntZTest.StepCounter.AntStepProcesser import AntStepProcesser
from AntenaProject.Common.Config.DictionaryConfigProvider import DictionaryConfigProvider

class StepCounter_tests(TestCase):
    def test__empty_ant(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        position_data=processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[0]==-1 and position_data[1]==-1 and position_data[2]==-1)
    def test__initial_ant(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        position_data=processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[0]==1 and position_data[1]==1 and position_data[2]==DirectionsEnum.North)

    def test__initial_ant_and_no_ant(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        position_data=processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[0]==1 and position_data[1]==1 and position_data[2]==DirectionsEnum.North)
        position_data = processor.get_ant_position_and_direction(100)
        self.assertTrue(position_data[0] == -1 and position_data[1] == -1 and position_data[2] == -1)

    def test__turn_left(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.North)
        processor.process_ant_step(99, StepEnum.TurnLeft)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.West)
        processor.process_ant_step(99, StepEnum.TurnLeft)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.South)
        processor.process_ant_step(99, StepEnum.TurnLeft)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.East)
        processor.process_ant_step(99, StepEnum.TurnLeft)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.North)

    def test__turn_right(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.North)
        processor.process_ant_step(99, StepEnum.TurnRight)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.East)
        processor.process_ant_step(99, StepEnum.TurnRight)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.South)
        processor.process_ant_step(99, StepEnum.TurnRight)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.West)
        processor.process_ant_step(99, StepEnum.TurnRight)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.North)

    def test__initial_step_turn(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.TurnRight)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[2] == DirectionsEnum.East)

    def test__from_north_step_forward(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.Forward)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[1] == 0)

    def test__from_north_step_back(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.Back)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[1] == 2)



    def test__from_south_step_forward(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.TurnLeft)
        processor.process_ant_step(99, StepEnum.TurnLeft)

        processor.process_ant_step(99, StepEnum.Forward)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[1] == 2)

    def test__from_south_step_back(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.TurnLeft)
        processor.process_ant_step(99, StepEnum.TurnLeft)

        processor.process_ant_step(99, StepEnum.Back)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[1] == 0)

    def test__from_east_step_forward(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.TurnRight)
        processor.process_ant_step(99, StepEnum.Forward)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[0] == 2)

    def test__from_east_step_back(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.TurnRight)
        processor.process_ant_step(99, StepEnum.Back)

        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[0] == 0)

    def test__from_west_step_forward(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.TurnLeft)

        processor.process_ant_step(99, StepEnum.Forward)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[0] == 0)

    def test__from_west_step_back(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.TurnLeft)

        processor.process_ant_step(99, StepEnum.Back)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[0] == 2)


    def test__complex_set_1(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.Back)
        processor.process_ant_step(99, StepEnum.Back)
        processor.process_ant_step(99, StepEnum.TurnRight)
        processor.process_ant_step(99, StepEnum.Forward)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[0] == 2)
        self.assertTrue(position_data[1] == 3)
        self.assertTrue(position_data[2] == DirectionsEnum.East)

    def test__complex_set_2(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.Back)
        processor.process_ant_step(99, StepEnum.Back)
        processor.process_ant_step(99, StepEnum.TurnRight)
        processor.process_ant_step(99, StepEnum.Forward)
        processor.process_ant_step(99, StepEnum.TurnRight)
        processor.process_ant_step(99, StepEnum.Back)
        position_data = processor.get_ant_position_and_direction(99)
        self.assertTrue(position_data[0] == 2)
        self.assertTrue(position_data[1] == 2)
        self.assertTrue(position_data[2] == DirectionsEnum.South)