from days import util, day7a


def test_example():
    lines = util.readinputfile('inputfiles/day7_example.txt')
    aligner = day7a.Aligner(lines[0])
    assert aligner.size() == 10
    alignment = aligner.calcbestx()
    assert alignment['bestx'] == 2
    assert alignment['totalfuels'][2] == 37
    assert alignment['totalfuels'][1] == 41
    assert alignment['totalfuels'][3] == 39
    assert alignment['totalfuels'][10] == 71
