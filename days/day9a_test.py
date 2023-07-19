from util import util
from days import day9a


def testExample():
    lines = util.readinputfile('inputfiles/day9_example.txt')
    heightmap = day9a.Heightmap(lines)

    assert heightmap.findlowpoints() == [1, 0, 5, 5]
    assert heightmap.calcrisklevel() == 15
