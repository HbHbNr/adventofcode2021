"""Unit tests for https://adventofcode.com/2021/day/14 part a"""
from util import util
from days import day14a


def testExample1():
    lines = util.readinputfile('inputfiles/day14_example.txt')
    polymer = day14a.Polymer(lines)

    assert str(polymer) == 'NNCB'

    results = ['NCNBCHB',
               'NBCCNBBBCBHCB',
               'NBBBCNCCNBBNBNBBCHBHHBCHB',
               'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB']
    for result in results:
        polymer.step()
        assert str(polymer) == result


def testExample2():
    lines = util.readinputfile('inputfiles/day14_example.txt')
    polymer = day14a.Polymer(lines)

    assert len(str(polymer)) == 4

    for _ in range(1, 5 + 1):
        polymer.step()
    assert len(str(polymer)) == 97

    for _ in range(6, 10 + 1):
        polymer.step()
    assert len(str(polymer)) == 3073


def testExample3():
    lines = util.readinputfile('inputfiles/day14_example.txt')
    polymer = day14a.Polymer(lines)

    for _ in range(1, 10 + 1):
        polymer.step()
    histogram = polymer.histogram()
    assert histogram.get('B') == 1749
    assert histogram.get('C') == 298
    assert histogram.get('H') == 161
    assert histogram.get('N') == 865

    values = list(histogram.values())
    values.sort()
    assert values[-1] - values[0] == 1588


def testInput():
    lines = util.readinputfile('inputfiles/day14_input.txt')
    polymer = day14a.Polymer(lines)
    for _ in range(1, 10 + 1):
        polymer.step()
    histogram = polymer.histogram()
    values = list(histogram.values())
    values.sort()
    assert values[-1] - values[0] == 2874
