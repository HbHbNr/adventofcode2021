"""Unit tests for https://adventofcode.com/2021/day/9 part a"""
from util import util
from days import day9a


def testExample():
    lines = util.readinputfile('inputfiles/day9_example.txt')
    heightmap = day9a.Heightmap(lines)

    assert heightmap.findlowpoints() == [1, 0, 5, 5]
    assert heightmap.calcrisklevel() == 15


def testInput():
    lines = util.readinputfile('inputfiles/day9_input.txt')
    heightmap = day9a.Heightmap(lines)

    assert heightmap.calcrisklevel() == 562
