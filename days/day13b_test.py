"""Unit tests for https://adventofcode.com/2021/day/13 part b"""
from util import util
from days import day13b


def testExample():
    lines = util.readinputfile('inputfiles/day13_example.txt')
    matrix = day13b.Matrix(lines)

    matrix.fold()
    assert matrix.countDots() == 16


def testInput():
    lines = util.readinputfile('inputfiles/day13_input.txt')
    matrix = day13b.Matrix(lines)

    matrix.fold()
    assert matrix.countDots() == 98
