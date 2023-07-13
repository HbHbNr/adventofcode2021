from util import util
from days import day11a


def test_example():
    lines = util.readinputfile('inputfiles/day11_example.txt')
    cavern = day11a.Cavern(lines)

    # note: all coordinates must respect the additional frame of 0s

    assert cavern.getTotalFlashes() == 0
    assert cavern.getEnergyLevel(1, 1) == 5  # top left
    assert cavern.getEnergyLevel(-2, -2) == 6  # bottom right

    cavern.step()  # step 1
    assert cavern.getTotalFlashes() == 0
    assert cavern.getEnergyLevel(1, 1) == 6  # top left
    assert cavern.getEnergyLevel(-2, -2) == 7  # bottom right

    cavern.step()  # step 2
    assert cavern.getTotalFlashes() == 35
    assert cavern.getEnergyLevel(1, 1) == 8  # top left
    assert cavern.getEnergyLevel(-2, -2) == 8  # bottom right

    for _ in range(3, 11):
        cavern.step()  # steps 3 to 10
    assert cavern.getTotalFlashes() == 204
    assert cavern.getEnergyLevel(1, 1) == 0  # top left
    assert cavern.getEnergyLevel(-2, -2) == 0  # bottom right

    for _ in range(11, 101):
        cavern.step()  # steps 11 to 100
    assert cavern.getTotalFlashes() == 1656
    assert cavern.getEnergyLevel(1, 1) == 0  # top left
    assert cavern.getEnergyLevel(-2, -2) == 6  # bottom right


def test_input():
    lines = util.readinputfile('inputfiles/day11_input.txt')
    cavern = day11a.Cavern(lines)

    # note: all coordinates must respect the additional frame of 0s

    for _ in range(1, 101):
        cavern.step()  # steps 1 to 100
    assert cavern.getTotalFlashes() == 1694
