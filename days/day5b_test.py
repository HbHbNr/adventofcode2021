from days import util, day5b


def test_map_example():
    lines = util.readinputfile('inputfiles/day5_example.txt')
    map = day5b.Map(lines)
    assert len(map._coords) == 10
    assert len(map._coords[0]) == 10
    assert map._coords[2][1] == 1
    assert map._coords[3][4] == 2
    assert map._coords[7][5] == 0
    assert map._coords[8][0] == 1
    assert map._coords[6][4] == 3
    assert map.countdangerouscoords() == 12
