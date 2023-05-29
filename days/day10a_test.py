from days import util, day10a


def test_brackets():
    assert day10a.Checker.isopenbracket('(') is True
    assert day10a.Checker.isopenbracket(')') is False
    assert day10a.Checker.matchingbrackets('[', ']') is True
    assert day10a.Checker.matchingbrackets('[', '}') is False
    assert day10a.Checker.errorscore('>') == 25137


def test_example():
    lines = util.readinputfile('inputfiles/day10_example.txt')
    checker = day10a.Checker(lines)
    syntaxerrors = checker.findsyntaxerrors()

    assert sum(syntaxerrors) == 26397
