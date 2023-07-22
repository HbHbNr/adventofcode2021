"""Unit tests for https://adventofcode.com/2021/day/2 part b"""
from days import day2b


def testInput():
    position = day2b.pilot()

    assert position.x * position.y == 1749524700
