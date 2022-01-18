from days import util, day4a


def test_bingoboard_simple():
    simplerows = ['1 2 3 4 5', '6 7 8 9 10', '11 12 13 14 15', '16 17 18 19 20', '21 22 23 24 25']
    bingoboard = day4a.BingoBoard(simplerows)
    assert bingoboard is not None


def test_bingoboard_example():
    lines = util.readinputfile('inputfiles/day4_example.txt')
    bingomatch = day4a.BingoMatch(lines)
    assert bingomatch is not None
