"""Unit tests for https://adventofcode.com/2021/day/8 part a"""
from util import util
from days import day08a


def testExample():
    lines = util.readinputfile('inputfiles/day08_example.txt')

    assert day08a.Panel(lines[0]).countdistinctdigits() == 2
    assert day08a.Panel(lines[-1]).countdistinctdigits() == 2
    assert day08a.Panel.countalldistinctdigits(lines) == 26


def testInput():
    lines = util.readinputfile('inputfiles/day08_input.txt')
    totalcount = day08a.Panel.countalldistinctdigits(lines)

    assert totalcount == 548
