from unittest import TestCase
from AntenaProject.AntZTest.StepCounter.Enums import DirectionsEnum
from AntenaProject.AntZTest.StepCounter.Enums import StepEnum
from AntenaProject.AntZTest.StepCounter.RobotAntPosition import RobotAntPosition
from AntenaProject.Common.Config.DictionaryConfigProvider import DictionaryConfigProvider
from AntenaProject.AntZTest.StepCounter.AntStepProcesser import AntStepProcesser
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.AntZTest.StepCounter.TranslateStep import TranslateStep

class TranslateStep_tests(TestCase):
    #Facing North
    def test__y_positive_north_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate=TranslateStep(config,processor)
        step=AntStep(99,Position(1,2))
        movment=translate.TranlateStep(step)
        self.assertTrue(len(movment) == 1)
        self.assertTrue(movment[0]==StepEnum.Back)

    def test__y_positive_south_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 1)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate=TranslateStep(config,processor)
        step=AntStep(99,Position(1,2))
        movment=translate.TranlateStep(step)
        self.assertTrue(movment[0]==StepEnum.Forward)

    def test__x_positive_north_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate=TranslateStep(config,processor)
        step=AntStep(99,Position(2,1))
        movment=translate.TranlateStep(step)
        self.assertTrue(len(movment) == 2)
        self.assertTrue(movment[0] == StepEnum.TurnRight)
        self.assertTrue(movment[1]==StepEnum.Forward)

    def test__x_negetive_north_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate = TranslateStep(config, processor)
        step = AntStep(99, Position(0, 1))
        movment = translate.TranlateStep(step)
        self.assertTrue(len(movment) == 2)
        self.assertTrue(movment[0] == StepEnum.TurnLeft)
        self.assertTrue(movment[1] == StepEnum.Forward)

    #Facing south
    def test__y_negetive_north_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 0)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate = TranslateStep(config, processor)
        step = AntStep(99, Position(1, 0))
        movment = translate.TranlateStep(step)
        self.assertTrue(len(movment) == 1)
        self.assertTrue(movment[0] == StepEnum.Forward)

    def test__y_negetive_south_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 1)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate = TranslateStep(config, processor)
        step = AntStep(99, Position(1, 0))
        movment = translate.TranlateStep(step)
        self.assertTrue(movment[0] == StepEnum.Back)

    def test__x_positive_south_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 1)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate=TranslateStep(config,processor)
        step=AntStep(99,Position(2,1))
        movment=translate.TranlateStep(step)
        self.assertTrue(len(movment) == 2)
        self.assertTrue(movment[0] == StepEnum.TurnLeft)
        self.assertTrue(movment[1]==StepEnum.Forward)

    def test__x_negetive_south_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 1)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate = TranslateStep(config, processor)
        step = AntStep(99, Position(0, 1))
        movment = translate.TranlateStep(step)
        self.assertTrue(len(movment) == 2)
        self.assertTrue(movment[0] == StepEnum.TurnRight)
        self.assertTrue(movment[1] == StepEnum.Forward)

    #facing east
    def test__y_positive_east_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection',2)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate=TranslateStep(config,processor)
        step=AntStep(99,Position(1,2))
        movment=translate.TranlateStep(step)
        self.assertTrue(len(movment) == 2)
        self.assertTrue(movment[0] == StepEnum.TurnRight)
        self.assertTrue(movment[1]==StepEnum.Forward)

    def test__y_negetive_east_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 2)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate=TranslateStep(config,processor)
        step=AntStep(99,Position(1,0))
        movment=translate.TranlateStep(step)
        self.assertTrue(len(movment) == 2)
        self.assertTrue(movment[0]==StepEnum.TurnLeft)
        self.assertTrue(movment[1] == StepEnum.Forward)

    def test__x_positive_east_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 2)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate=TranslateStep(config,processor)
        step=AntStep(99,Position(2,1))
        movment=translate.TranlateStep(step)
        self.assertTrue(len(movment) == 1)
        self.assertTrue(movment[0]==StepEnum.Forward)

    def test__x_negetive_east_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 2)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate = TranslateStep(config, processor)
        step = AntStep(99, Position(0, 1))
        movment = translate.TranlateStep(step)
        self.assertTrue(len(movment) == 1)

        self.assertTrue(movment[0] == StepEnum.Back)

    # facing west

    def test__y_positive_west_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 3)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate = TranslateStep(config, processor)
        step = AntStep(99, Position(1, 2))
        movment = translate.TranlateStep(step)
        self.assertTrue(len(movment) == 2)
        self.assertTrue(movment[0] == StepEnum.TurnLeft)
        self.assertTrue(movment[1] == StepEnum.Forward)

    def test__y_negetive_west_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 3)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate = TranslateStep(config, processor)
        step = AntStep(99, Position(1, 0))
        movment = translate.TranlateStep(step)
        self.assertTrue(len(movment) == 2)
        self.assertTrue(movment[0] == StepEnum.TurnRight)
        self.assertTrue(movment[1] == StepEnum.Forward)

    def test__x_positive_west_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 3)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate = TranslateStep(config, processor)
        step = AntStep(99, Position(2, 1))
        movment = translate.TranlateStep(step)
        self.assertTrue(len(movment) == 1)
        self.assertTrue(movment[0] == StepEnum.Back)

    def test__x_negetive_west_facing_axis_movment(self):
        config = DictionaryConfigProvider()
        config.SetValue('InitialPosition', 'InitialDirection', 3)
        config.SetValue('InitialPosition', 'InitialPosition_x', 1)
        config.SetValue('InitialPosition', 'InitialPosition_y', 1)
        processor = AntStepProcesser(config)
        processor.process_ant_step(99, StepEnum.NoStep)
        translate = TranslateStep(config, processor)
        step = AntStep(99, Position(0, 1))
        movment = translate.TranlateStep(step)
        self.assertTrue(len(movment) == 1)

        self.assertTrue(movment[0] == StepEnum.Forward)



