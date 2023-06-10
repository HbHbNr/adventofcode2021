from days import util, day13a


def test_example1():
    lines = util.readinputfile('inputfiles/day13_example.txt')
    matrix = day13a.Matrix(lines)
    matrix.fold(1)

    assert matrix.countDots() == 17


def test_input():
    lines = util.readinputfile('inputfiles/day13_input.txt')
    matrix = day13a.Matrix(lines)
    matrix.fold(1)

    assert matrix.countDots() == 675
