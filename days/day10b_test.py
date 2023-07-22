from util import util
from days import day10b


def testBrackets():
    assert day10b.Checker.isopenbracket('(') is True
    assert day10b.Checker.isopenbracket(')') is False
    assert day10b.Checker.matchingbrackets('[', ']') is True
    assert day10b.Checker.matchingbrackets('[', '}') is False
    assert day10b.Checker.scoreofbracket('<') == 4


def testExample():
    lines = util.readinputfile('inputfiles/day10_example.txt')
    checker = day10b.Checker(lines)
    incompletelines = checker.findincompletelines()

    assert len(incompletelines) == 5
    assert incompletelines[4] == list("<{([")
    assert day10b.Checker.calccompletescore(incompletelines) == 288957


def testInput():
    lines = util.readinputfile('inputfiles/day10_input.txt')
    checker = day10b.Checker(lines)
    incompletelines = checker.findincompletelines()

    assert day10b.Checker.calccompletescore(incompletelines) == 3249889609
