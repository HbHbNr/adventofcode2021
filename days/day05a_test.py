"""Unit tests for https://adventofcode.com/2021/day/5 part a"""
from util import util
from days import day05a


def testMapExample():
    lines = util.readinputfile('inputfiles/day5_example.txt')
    theMap = day05a.Map(lines)
    # assert len(theMap._coords) == 10
    # assert len(theMap._coords[0]) == 10

    assert theMap.testCoord(2, 1, 1)
    assert theMap.testCoord(3, 4, 2)
    assert theMap.testCoord(7, 5, 0)
    assert theMap.countdangerouscoords() == 5


def testMapInput():
    lines = util.readinputfile('inputfiles/day5_input.txt')
    theMap = day05a.Map(lines)

    assert theMap.countdangerouscoords() == 5698
