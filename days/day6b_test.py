from util import util
from days import day6b


def test_example():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6b.School(lines[0])
    assert school.size() == 5
    school.nextday()
    assert school.size() == 5
    school.nextday()
    assert school.size() == 6


def test_example18():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6b.School(lines[0])
    school.nextdays(18)
    assert school.size() == 26


def test_example80():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6b.School(lines[0])
    school.nextdays(80)
    assert school.size() == 5934
