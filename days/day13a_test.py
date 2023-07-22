"""Unit tests for https://adventofcode.com/2021/day/13 part a"""
from util import util
from days import day13a


def testExample():
    lines = util.readinputfile('inputfiles/day13_example.txt')
    matrix = day13a.Matrix(lines)

    assert matrix.countDots() == 17


def testInput():
    lines = util.readinputfile('inputfiles/day13_input.txt')
    matrix = day13a.Matrix(lines)

    assert matrix.countDots() == 675
