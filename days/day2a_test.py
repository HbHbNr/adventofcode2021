from days import day2a


def testInput():
    position = day2a.pilot()

    assert position.x * position.y == 1692075
