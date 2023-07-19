from util import util
from days import day5b


def testMapExample():
    lines = util.readinputfile('inputfiles/day5_example.txt')
    theMap = day5b.Map(lines)
    # assert len(theMap._coords) == 10
    # assert len(theMap._coords[0]) == 10
    assert theMap.testCoord(2, 1, 1)
    assert theMap.testCoord(3, 4, 2)
    assert theMap.testCoord(7, 5, 0)
    assert theMap.testCoord(8, 0, 1)
    assert theMap.testCoord(6, 4, 3)
    assert theMap.countdangerouscoords() == 12
