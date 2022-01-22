from days import util, day5a


def test_map_example():
    lines = util.readinputfile('inputfiles/day5_example.txt')
    map = day5a.Map(lines)
    assert len(map._coords) == 10
    assert len(map._coords[0]) == 10
