"""Unit tests for https://adventofcode.com/2021/day/10 part a"""
from util import util
from days import day10a


def testBrackets():
    assert day10a.Checker.isopenbracket('(') is True
    assert day10a.Checker.isopenbracket(')') is False
    assert day10a.Checker.matchingbrackets('[', ']') is True
    assert day10a.Checker.matchingbrackets('[', '}') is False
    assert day10a.Checker.errorscore('>') == 25137


def testExample():
    lines = util.readinputfile('inputfiles/day10_example.txt')
    checker = day10a.Checker(lines)
    syntaxerrors = checker.findsyntaxerrors()

    assert sum(syntaxerrors) == 26397


def testInput():
    lines = util.readinputfile('inputfiles/day10_input.txt')
    checker = day10a.Checker(lines)
    syntaxerrors = checker.findsyntaxerrors()

    assert sum(syntaxerrors) == 370407
