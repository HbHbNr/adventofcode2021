from days import day2b


def testInput():
    position = day2b.pilot()

    assert position.x * position.y == 1749524700
