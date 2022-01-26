from days import util, day8a


def test_example():
    lines = util.readinputfile('inputfiles/day8_example.txt')

    assert day8a.Panel(lines[0]).countdistinctdigits() == 2
    assert day8a.Panel(lines[-1]).countdistinctdigits() == 2
    assert day8a.Panel.countalldistinctdigits(lines) == 26
