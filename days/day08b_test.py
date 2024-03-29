"""Unit tests for https://adventofcode.com/2021/day/8 part b"""
from util import util
from days import day08b


def testExampleDistinct():
    lines = util.readinputfile('inputfiles/day08_example.txt')

    assert day08b.Panel(lines[0]).countdistinctdigits() == 2
    assert day08b.Panel(lines[-1]).countdistinctdigits() == 2
    assert day08b.Panel.countalldistinctdigits(lines) == 26


def testExampleOutput():
    lines = util.readinputfile('inputfiles/day08_example.txt')

    assert day08b.Panel(lines[0]).output() == 8394
    assert day08b.Panel(lines[-1]).output() == 4315

    assert day08b.Panel.sumoutputs(lines) == 61229


def testInput():
    lines = util.readinputfile('inputfiles/day08_input.txt')
    totalsum = day08b.Panel.sumoutputs(lines)

    assert totalsum == 1074888
