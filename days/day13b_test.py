from days import util, day13b


def test_example1():
    lines = util.readinputfile('inputfiles/day13_example.txt')
    matrix = day13b.Matrix(lines)

    matrix.fold()
    assert matrix.countDots() == 16


def test_input():
    lines = util.readinputfile('inputfiles/day13_input.txt')
    matrix = day13b.Matrix(lines)

    matrix.fold()
    assert matrix.countDots() == 98
