from util import util
from days import day4a


def testBingoBoardSimple():
    simplerows = ['1 2 3 4 5', '6 7 8 9 10', '11 12 13 14 15', '16 17 18 19 20', '21 22 23 24 25']
    bingoboard = day4a.BingoBoard(simplerows)

    assert bingoboard.sum() == sum(range(26))
    assert bingoboard.getRow(1) == (6, 7, 8, 9, 10)
    assert bingoboard.getColumn(2) == (3, 8, 13, 18, 23)


def testBingoMatchExample():
    lines = util.readinputfile('inputfiles/day4_example.txt')
    bingomatch = day4a.BingoMatch(lines)
    result = bingomatch.play()

    assert result is not None
    assert result['numberindex'] == 11
    assert result['pickednumber'] == 24
    assert result['boardindex'] == 2
    assert result['boardsum'] == 188
    assert result['solution'] == 4512


def testBingoMatchInput():
    lines = util.readinputfile('inputfiles/day4_input.txt')
    bingomatch = day4a.BingoMatch(lines)
    result = bingomatch.play()

    assert result['pickednumber'] * result['boardsum'] == 58838
