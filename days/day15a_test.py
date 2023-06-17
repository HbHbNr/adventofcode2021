from days import util, day15a


def test_example1():
    lines = ['1163', '1381', '2136', '3694']  # top left of example
    riskMap = day15a.RiskMap(lines)
    lowestRiskPath = riskMap.findLowestRiskPath()
    actualLowestRiskPath = [int(c) for c in '12136']  # start point not included

    assert len(lowestRiskPath) == len(actualLowestRiskPath)
    assert sum(lowestRiskPath) == sum(actualLowestRiskPath)
    assert lowestRiskPath == actualLowestRiskPath


def test_example2():
    lines = util.readinputfile('inputfiles/day15_example.txt')
    riskMap = day15a.RiskMap(lines)
    lowestRiskPath = riskMap.findLowestRiskPath()
    actualLowestRiskPath = [int(c) for c in '121365111511323211']  # start point not included

    assert len(lowestRiskPath) == len(actualLowestRiskPath)
    assert sum(lowestRiskPath) == sum(actualLowestRiskPath)
    assert lowestRiskPath == actualLowestRiskPath


# def test_input():
#     lines = util.readinputfile('inputfiles/day15_input.txt')
#     riskMap = day15a.RiskMap(lines)
#     lowestRiskPath = riskMap.findLowestRiskPath()
#
#     assert sum(lowestRiskPath) == ???
