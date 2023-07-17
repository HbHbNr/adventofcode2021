from util import util
from days import day5a


def test_map_example():
    lines = util.readinputfile('inputfiles/day5_example.txt')
    theMap = day5a.Map(lines)
    # assert len(theMap._coords) == 10
    # assert len(theMap._coords[0]) == 10
    assert theMap.testCoord(2, 1, 1)
    assert theMap.testCoord(3, 4, 2)
    assert theMap.testCoord(7, 5, 0)
    assert theMap.countdangerouscoords() == 5
