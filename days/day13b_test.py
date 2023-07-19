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
