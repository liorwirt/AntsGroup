from unittest import  TestCase

import numpy as np
from AntenaProject.Common.Maze.DummyMazeParser import DummyMazeParser
from AntenaProject.Common.Maze.FixedMazeParser import FixedMazeParser
from AntenaProject.Common.Maze.FileMazeParser import FileMazeParser

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
        self.assertTrue(mazeparser.GetEnterence()==(0,0))

    def test_Fixed_Exits(self):
        mazeparser = FixedMazeParser()
        exits=mazeparser.GetExits()
        self.assertTrue(exits[0]==(4,4))
        self.assertTrue(exits[1] == (4, 2))

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
        self.assertTrue(mazeparser.GetEnterence()==(0,0))

    def test_File__many_Exits(self):
        mazeparser =FileMazeParser("map_ManyExits.txt")
        exits=mazeparser.GetExits()
        self.assertTrue(len(exits[0]) >1)
        self.assertTrue(exits[0]==(4,0))

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