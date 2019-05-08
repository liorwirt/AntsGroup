from unittest import  TestCase
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.Maze.Parsers.DummyMazeParser import DummyMazeParser
from AntenaProject.Common.Maze.Parsers.FixedMazeParser import FixedMazeParser
from AntenaProject.Common.Maze.Parsers.FileMazeParser import FileMazeParser
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade

class TestMazeParserDummy(TestCase):
    def test_dummy_dims(self):
        mazeparser=DummyMazeParser()
        self.assertEqual(mazeparser.GetDims(), (0,0))

    def test_dummy_emptyMatrix(self):
        mazeparser = DummyMazeParser()
        self.assertEqual(mazeparser.GetMatrix(), None)

class TestMazeParserFixed(TestCase):
    def test_Fixed_NotEmpty(self):
        mazeparser = FixedMazeParser()
        self.assertTrue(mazeparser.GetMatrix().any())

    def test_Fixed_Dims(self):
        mazeparser = FixedMazeParser()
        self.assertTrue(mazeparser.GetDims()==(5,5))

    def test_Fixed_Entrence(self):
        mazeparser = FixedMazeParser()
        self.assertTrue(mazeparser.GetEnterence()==Position(0,0))

    def test_Fixed_Exits(self):
        mazeparser = FixedMazeParser()
        exits=mazeparser.GetExits()
        self.assertTrue(exits[0]==Position(4,4))
        self.assertTrue(exits[1] == Position(4, 2))

    def test_Fixed_Obs(self):
        mazeparser = FixedMazeParser()
        matrix=mazeparser.GetMatrix()
        self.assertTrue(matrix[2][1]==0)

class TestMazeParserFile(TestCase):
    def test_NoFile(self):
        with self.assertRaises(Exception) as context:
            mazeparser=FileMazeParser("nofile.txt")

        self.assertTrue(  len(context.exception.args)==1)
    def test_File_NotEmpty(self):
        mazeparser =FileMazeParser("map_regular.txt")
        self.assertTrue(mazeparser.GetMatrix().any())

    def test_File_Dims(self):
        mazeparser =FileMazeParser("map_regular.txt")
        self.assertTrue(mazeparser.GetDims()==(31,31))

    def test_File_Entrence(self):
        mazeparser = FileMazeParser("map_regular.txt")
        self.assertTrue(mazeparser.GetEnterence()==Position(0,0))

    def test_File__many_Exits(self):
        mazeparser =FileMazeParser("map_ManyExits.txt")
        exits=mazeparser.GetExits()
        self.assertTrue(len(exits) >1)
        self.assertTrue(exits[0]==Position(4,0))

    def test_File__NoEntrence(self):
        with self.assertRaises(Exception) as context:
            mazeparser = FileMazeParser("map_NoEnterence.txt")

        self.assertTrue(len(context.exception.args) == 1)

    def test_File__NoExits(self):
        with self.assertRaises(Exception) as context:
            mazeparser = FileMazeParser("map_NoExits.txt")
        self.assertTrue(len(context.exception.args) == 1)

    def test_File_Obs_1(self):
        mazeparser =FileMazeParser("map_regular.txt")
        matrix=mazeparser.GetMatrix()
        self.assertTrue(matrix[3][3]==0)

    def test_File_Obs_2(self):
        mazeparser =FileMazeParser("map_regular.txt")
        matrix = mazeparser.GetMatrix()
        self.assertTrue(matrix[28][30] == 0)

class TestMazeFacade(TestCase):
    def setUp(self):
        self.__mazeparser = FileMazeParser("map_regular.txt")


    def test_MazeFacade_NotEmpty(self):
        mazeFacade = MazeFacade(self.__mazeparser)
        self.assertTrue(mazeFacade.GetMatrix().any())

    def test_MazeFacade_Dims(self):
        mazeFacade = MazeFacade(self.__mazeparser)

        self.assertTrue(mazeFacade.GetDims() == (31, 31))

    def test_MazeFacade_Entrence(self):
        mazeFacade = MazeFacade(self.__mazeparser)
        self.assertTrue(mazeFacade.GetEnterence() == Position(0, 0))

    def test_MazeFacade_mayMove_True_1(self):
        mazeFacade = MazeFacade(self.__mazeparser)
        self.assertTrue(mazeFacade.MayMove(src=Position(0,0),dst=Position(1,0)))

    def test_MazeFacade_mayMove_True_2(self):
        mazeFacade = MazeFacade(self.__mazeparser)
        self.assertTrue(mazeFacade.MayMove(src=Position(14,8),dst=Position(15,8)))

    def test_MazeFacade_mayMove_False_Node_Not_InGrpah(self):
        mazeFacade = MazeFacade(self.__mazeparser)
        self.assertFalse(mazeFacade.MayMove(src=Position(2, 1), dst=Position(2, 2)))

    def test_MazeFacade_mayMove_False_Path_Too_Long(self):
        mazeFacade = MazeFacade(self.__mazeparser)
        self.assertFalse(mazeFacade.MayMove(src=Position(2, 1), dst=Position(2, 6)))

    def test_MazeFacade_mayMove_SamePoint(self):
        mazeFacade = MazeFacade(self.__mazeparser)
        self.assertTrue(mazeFacade.MayMove(src=Position(0,0),dst=Position(0,0)))

