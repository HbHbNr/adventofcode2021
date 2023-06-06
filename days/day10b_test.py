from days import util, day10b


def test_brackets():
    assert day10b.Checker.isopenbracket('(') is True
    assert day10b.Checker.isopenbracket(')') is False
    assert day10b.Checker.matchingbrackets('[', ']') is True
    assert day10b.Checker.matchingbrackets('[', '}') is False
    assert day10b.Checker.scoreofbracket('<') == 4


def test_example():
    lines = util.readinputfile('inputfiles/day10_example.txt')
    checker = day10b.Checker(lines)
    incompletelines = checker.findincompletelines()

    assert len(incompletelines) == 5
    assert incompletelines[4] == list("<{([")
    assert day10b.Checker.calccompletescore(incompletelines) == 288957