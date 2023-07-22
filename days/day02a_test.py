"""Unit tests for https://adventofcode.com/2021/day/2 part a"""
from days import day02a


def testInput():
    position = day02a.pilot()

    assert position.x * position.y == 1692075
