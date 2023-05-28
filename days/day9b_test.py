from days import util, day9b


def test_example():
    lines = util.readinputfile('inputfiles/day9_example.txt')
    heightmap = day9b.Heightmap(lines)
    basins = heightmap.findbasins()
    top3product = int(basins[0]) * int(basins[1]) * int(basins[2])

    assert basins == [14, 9, 9, 3]
    assert top3product == 14 * 9 * 9
