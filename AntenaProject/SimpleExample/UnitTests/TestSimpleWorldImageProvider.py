from unittest import  TestCase
from AntenaProject.Common.Config.DictionaryConfigProvider import DictionaryConfigProvider
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.Maze.Parsers.DIYMazeParser import DIYMazeParser
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.SimpleExample.SimpleWorldImageProvider import SimpleWorldImageProvider
from AntenaProject.SimpleExample.UnitTests.RemoteControlledAnt import RemoteControlledAnt
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep

class TestMazeParserDummy(TestCase):
    def setUp(self):
        self.__Config= config=DictionaryConfigProvider()
        config.SetValue("SimpleAnt", "VisibilityRange", 2)
        config.SetValue("SimpleAnt", "AllowedMovement", 1)

    def test_GetAntWorldImage_NoObs_TopLeftCorner(self):
        mazeparser=DIYMazeParser(5)
        mazeparser.SetExits([Position(4,4)])
        mazefacade=MazeFacade(mazeparser)
        WorldImageProvider=SimpleWorldImageProvider(self.__Config, mazefacade)
        ant=RemoteControlledAnt(1,self.__Config)
        ant.UpdatePosition(position=Position(0,0))
        antworldimage=WorldImageProvider.GetAntWorldImage(ant)
        self.assertTrue(len(antworldimage.VisibleNodes)==9)

    def test_GetAntWorldImage_NoObs_TopRightCorner(self):
        mazeparser = DIYMazeParser(5)
        mazeparser.SetExits([Position(4, 4)])
        mazefacade = MazeFacade(mazeparser)
        WorldImageProvider = SimpleWorldImageProvider(self.__Config, mazefacade)
        ant = RemoteControlledAnt(1, self.__Config)
        ant.UpdatePosition(position=Position(4, 0))
        antworldimage = WorldImageProvider.GetAntWorldImage(ant)
        self.assertTrue(len(antworldimage.VisibleNodes) == 9)

    def test_GetAntWorldImage_NoObs_BottomLeftCorner(self):
        mazeparser = DIYMazeParser(5)
        mazeparser.SetExits([Position(4, 4)])
        mazefacade = MazeFacade(mazeparser)
        WorldImageProvider = SimpleWorldImageProvider(self.__Config, mazefacade)
        ant = RemoteControlledAnt(1, self.__Config)
        ant.UpdatePosition(position=Position(0, 4))
        antworldimage = WorldImageProvider.GetAntWorldImage(ant)
        self.assertTrue(len(antworldimage.VisibleNodes) == 9)

    def test_GetAntWorldImage_NoObs_BottomRightCorner(self):
        mazeparser = DIYMazeParser(5)
        mazeparser.SetExits([Position(4, 4)])
        mazefacade = MazeFacade(mazeparser)
        WorldImageProvider = SimpleWorldImageProvider(self.__Config, mazefacade)
        ant = RemoteControlledAnt(1, self.__Config)
        ant.UpdatePosition(position=Position(4, 4))
        antworldimage = WorldImageProvider.GetAntWorldImage(ant)
        self.assertTrue(len(antworldimage.VisibleNodes) == 9)

    def test_GetAntWorldImage_NoObs_Center_1(self):
        mazeparser = DIYMazeParser(5)
        mazeparser.SetExits([Position(4, 4)])
        mazefacade = MazeFacade(mazeparser)
        WorldImageProvider = SimpleWorldImageProvider(self.__Config, mazefacade)
        ant = RemoteControlledAnt(1, self.__Config)
        ant.UpdatePosition(position=Position(3, 3))
        antworldimage = WorldImageProvider.GetAntWorldImage(ant)
        self.assertTrue(len(antworldimage.VisibleNodes) == 16)

    def test_GetAntWorldImage_NoObs_Center_2(self):
        mazeparser = DIYMazeParser(5)
        mazeparser.SetExits([Position(4, 4)])
        mazefacade = MazeFacade(mazeparser)
        WorldImageProvider = SimpleWorldImageProvider(self.__Config, mazefacade)
        ant = RemoteControlledAnt(1, self.__Config)
        ant.UpdatePosition(position=Position(2, 1))
        antworldimage = WorldImageProvider.GetAntWorldImage(ant)
        self.assertTrue(len(antworldimage.VisibleNodes) == 20)

    def test_UpdateStep_SeeObs(self):
        mazeparser = DIYMazeParser(5)
        mazeparser.SetExits([Position(4, 4)])
        mazeparser.SetObs([Position(3, 3)])
        mazefacade = MazeFacade(mazeparser)
        WorldImageProvider = SimpleWorldImageProvider(self.__Config, mazefacade)
        ant = RemoteControlledAnt(1, self.__Config)
        ant.UpdatePosition(position=Position(4, 4))
        WorldImageProvider.ProcessStep(ant,AntStep(1,Position(4,4)))
        WorldImageProvider.UpdatePositionsAccordingToMoves()
        antworldimage = WorldImageProvider.GetAntWorldImage(ant)
        obsList = list(filter(lambda x: x.NodeState == NodeStateEnum.Obs, antworldimage.VisibleNodes))
        self.assertTrue(len(obsList) == 1)

