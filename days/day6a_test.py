from util import util
from days import day6a


def testExample():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6a.School(lines[0])

    assert school.size() == 5
    assert school.getFishes() == (3, 4, 3, 1, 2)

    school.nextday()

    assert school.size() == 5
    assert school.getFishes() == (2, 3, 2, 0, 1)

    school.nextday()

    assert school.size() == 6
    assert school.getFishes() == (1, 2, 1, 6, 0, 8)


def testExample18():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6a.School(lines[0])
    school.nextdays(18)

    assert school.size() == 26

    fishes = school.getFishes()

    assert fishes[2] == 6
    assert fishes[21] == 7
    assert fishes[22] == 8


def testExample80():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6a.School(lines[0])
    school.nextdays(80)

    assert school.size() == 5934


def testInput():
    lines = util.readinputfile('inputfiles/day6_input.txt')
    school = day6a.School(lines[0])
    school.nextdays(80, False)

    assert school.size() == 377263
