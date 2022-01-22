from days import util, day5a


def test_map_example():
    lines = util.readinputfile('inputfiles/day5_example.txt')
    map = day5a.Map(lines)
    assert len(map._coords) == 10
    assert len(map._coords[0]) == 10
    assert map._coords[2][1] == 1
    assert map._coords[3][4] == 2
    assert map._coords[7][5] == 0
    assert map.countdangerouscoords() == 5
