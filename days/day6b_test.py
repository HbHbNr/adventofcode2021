from util import util
from days import day6b


def testExample():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6b.School(lines[0])
    assert school.size() == 5
    school.nextday()
    assert school.size() == 5
    school.nextday()
    assert school.size() == 6


def testExample18():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6b.School(lines[0])
    school.nextdays(18)
    assert school.size() == 26


def testExample80():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6b.School(lines[0])
    school.nextdays(80)
    assert school.size() == 5934


def testInput():
    lines = util.readinputfile('inputfiles/day6_input.txt')
    school = day6b.School(lines[0])
    school.nextdays(256, False)

    assert school.size() == 1695929023803
