"""Unit tests for https://adventofcode.com/2021/day/7 part b"""
from util import util
from days import day7b


def testExample():
    lines = util.readinputfile('inputfiles/day7_example.txt')
    aligner = day7b.Aligner(lines[0])

    assert aligner.size() == 10

    alignment = aligner.calcbestx()

    assert alignment['bestx'] == 5
    assert alignment['totalfuels'][2] == 206
    assert alignment['totalfuels'][5] == 168


def testInput():
    lines = util.readinputfile('inputfiles/day7_input.txt')
    aligner = day7b.Aligner(lines[0])
    alignment = aligner.calcbestx()

    assert alignment['totalfuels'][alignment['bestx']] == 96987874
