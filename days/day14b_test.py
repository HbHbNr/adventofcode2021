from days import util, day14b


def test_example1():
    lines = util.readinputfile('inputfiles/day14_example.txt')
    polymer = day14b.Polymer(lines)
    polymer.steps(0)
    histogram = polymer.histogram()
    assert histogram.get('B') == 1
    assert histogram.get('C') == 1
    assert histogram.get('H') == 0
    assert histogram.get('N') == 2


def test_example2():
    lines = util.readinputfile('inputfiles/day14_example.txt')
    polymer = day14b.Polymer(lines)
    polymer = day14b.Polymer(lines)
    polymer.steps(4)
    histogram = polymer.histogram()
    assert histogram.get('B') == 23
    assert histogram.get('C') == 10
    assert histogram.get('H') == 5
    assert histogram.get('N') == 11

    values = list(histogram.values())
    values.sort()
    assert values[-1] - values[0] == 18


def test_example3():
    lines = util.readinputfile('inputfiles/day14_example.txt')
    polymer = day14b.Polymer(lines)
    polymer.steps(10)
    histogram = polymer.histogram()
    assert histogram.get('B') == 1749
    assert histogram.get('C') == 298
    assert histogram.get('H') == 161
    assert histogram.get('N') == 865

    values = list(histogram.values())
    values.sort()
    assert values[-1] - values[0] == 1588


# TOO SLOW!
def ttest_example4():
    lines = util.readinputfile('inputfiles/day14_example.txt')
    polymer = day14b.Polymer(lines)
    polymer.steps(40)
    histogram = polymer.histogram()
    assert histogram.get('B') == 2192039569602
    assert histogram.get('H') == 3849876073

    values = list(histogram.values())
    values.sort()
    assert values[-1] - values[0] == 2188189693529


# def test_input():
#     lines = util.readinputfile('inputfiles/day14_input.txt')
#     polymer = day14b.Polymer(lines)
#     for step in range(1, 10 + 1):
#         polymer.step()
#     histogram = polymer.histogram()
#     values = list(histogram.values())
#     values.sort()
#     assert values[-1] - values[0] == 2874
