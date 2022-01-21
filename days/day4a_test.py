from days import util, day4a


def test_bingoboard_simple():
    simplerows = ['1 2 3 4 5', '6 7 8 9 10', '11 12 13 14 15', '16 17 18 19 20', '21 22 23 24 25']
    bingoboard = day4a.BingoBoard(simplerows)
    assert bingoboard.sum() == sum(range(26))
    assert bingoboard._rows[1] == [6, 7, 8, 9, 10]
    assert bingoboard._columns[2] == [3, 8, 13, 18, 23]


def test_bingomatch_example():
    lines = util.readinputfile('inputfiles/day4_example.txt')
    bingomatch = day4a.BingoMatch(lines)
    result = bingomatch.play()
    assert result is not None
    assert result['numberindex'] == 11
    assert result['pickednumber'] == 24
    assert result['boardindex'] == 2
    assert result['boardsum'] == 188
    assert result['solution'] == 4512
