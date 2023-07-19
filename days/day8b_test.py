from util import util
from days import day8b


def testExampleDistinct():
    lines = util.readinputfile('inputfiles/day8_example.txt')

    assert day8b.Panel(lines[0]).countdistinctdigits() == 2
    assert day8b.Panel(lines[-1]).countdistinctdigits() == 2
    assert day8b.Panel.countalldistinctdigits(lines) == 26


def testExampleOutput():
    lines = util.readinputfile('inputfiles/day8_example.txt')

    assert day8b.Panel(lines[0]).output() == 8394
    assert day8b.Panel(lines[-1]).output() == 4315

    assert day8b.Panel.sumoutputs(lines) == 61229
