"""Unit tests for https://adventofcode.com/2021/day/7 part a"""
from util import util
from days import day7a


def testExample():
    lines = util.readinputfile('inputfiles/day7_example.txt')
    aligner = day7a.Aligner(lines[0])
    assert aligner.size() == 10
    alignment = aligner.calcbestx()
    assert alignment['bestx'] == 2
    assert alignment['totalfuels'][2] == 37
    assert alignment['totalfuels'][1] == 41
    assert alignment['totalfuels'][3] == 39
    assert alignment['totalfuels'][10] == 71


def testInput():
    lines = util.readinputfile('inputfiles/day7_input.txt')
    aligner = day7a.Aligner(lines[0])
    alignment = aligner.calcbestx()

    assert alignment['totalfuels'][alignment['bestx']] == 340987
