from days import util, day8a


def test_example():
    lines = util.readinputfile('inputfiles/day8_example.txt')
    digitmap = day8a.DigitMap()

    assert day8a.Panel(digitmap, lines[0]).countdistinctdigits() == 2
    assert day8a.Panel(digitmap, lines[-1]).countdistinctdigits() == 2

    totalcount = 0
    for line in lines:
        panel = day8a.Panel(digitmap, line)
        totalcount += panel.countdistinctdigits()
    assert totalcount == 26
