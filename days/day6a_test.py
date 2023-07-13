from util import util
from days import day6a


def test_example():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6a.School(lines[0])
    assert school.size() == 5
    assert school._fishes == [3, 4, 3, 1, 2]
    school.nextday()
    assert school.size() == 5
    assert school._fishes == [2, 3, 2, 0, 1]
    school.nextday()
    assert school.size() == 6
    assert school._fishes == [1, 2, 1, 6, 0, 8]


def test_example18():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6a.School(lines[0])
    school.nextdays(18)
    assert school.size() == 26
    assert school._fishes[2] == 6
    assert school._fishes[21] == 7
    assert school._fishes[22] == 8


def test_example80():
    lines = util.readinputfile('inputfiles/day6_example.txt')
    school = day6a.School(lines[0])
    school.nextdays(80)
    assert school.size() == 5934
