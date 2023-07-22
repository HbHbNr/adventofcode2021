"""Unit tests for https://adventofcode.com/2021/day/3 part a"""
from days import day03a


def testInput():
    # inputfile = "inputfiles/day3_example.txt"
    inputfile = "inputfiles/day3_input.txt"

    histogram = day03a.createhistogram(inputfile)
    gamma = histogram.buildparameter(True)
    epsilon = histogram.buildparameter(False)

    assert int(gamma, 2) * int(epsilon, 2) == 738234
