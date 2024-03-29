"""Unit tests for https://adventofcode.com/2021/day/3 part b"""
from days import day03b


def testDetermineratings():
    oxygen, co2 = day03b.determineratings('inputfiles/day03_example.txt')

    assert oxygen == '10111'
    assert co2 == '01010'
    assert int(oxygen, 2) * int(co2, 2) == 230


def testInput():
    oxygen, co2 = day03b.determineratings('inputfiles/day03_input.txt')

    assert int(oxygen, 2) * int(co2, 2) == 3969126
