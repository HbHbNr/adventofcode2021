from days import util, day9a


def test_example():
    lines = util.readinputfile('inputfiles/day9_example.txt')
    heightmap = day9a.Heightmap(lines)

    assert heightmap.lowPoints() == [1, 0, 5, 5]
    assert heightmap.riskLevel() == 15
