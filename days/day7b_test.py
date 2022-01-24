from days import util, day7b


def test_example():
    lines = util.readinputfile('inputfiles/day7_example.txt')
    aligner = day7b.Aligner(lines[0])
    assert aligner.size() == 10
    alignment = aligner.calcbestx()
    assert alignment['bestx'] == 5
    assert alignment['totalfuels'][2] == 206
    assert alignment['totalfuels'][5] == 168
