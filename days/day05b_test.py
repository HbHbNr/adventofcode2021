"""Unit tests for https://adventofcode.com/2021/day/5 part b"""
from util import util
from days import day05b


def testMapExample():
    lines = util.readinputfile('inputfiles/day05_example.txt')
    theMap = day05b.Map(lines)

    # assert len(theMap._coords) == 10
    # assert len(theMap._coords[0]) == 10
    assert theMap.testCoord(2, 1, 1)
    assert theMap.testCoord(3, 4, 2)
    assert theMap.testCoord(7, 5, 0)
    assert theMap.testCoord(8, 0, 1)
    assert theMap.testCoord(6, 4, 3)
    assert theMap.countdangerouscoords() == 12


def testMapInput():
    lines = util.readinputfile('inputfiles/day05_input.txt')
    theMap = day05b.Map(lines)

    assert theMap.countdangerouscoords() == 15463
