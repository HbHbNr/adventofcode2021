from days import util, day11a


def test_example():
    lines = util.readinputfile('inputfiles/day11_example.txt')
    cavern = day11a.Cavern(lines)

    assert cavern.totalFlashes() == 0

    cavern.step()  # step 1
    assert cavern.totalFlashes() == 0
    assert cavern.getEnergyLevel(0, 0) == 6  # top left
    assert cavern.getEnergyLevel(-1, -1) == 7  # bottom right

    cavern.step()  # step 2
    assert cavern.totalFlashes() == 35
    assert cavern.getEnergyLevel(0, 0) == 8  # top left
    assert cavern.getEnergyLevel(-1, -1) == 8  # bottom right

    for step in range(3, 11):
        cavern.step()  # steps 3 to 10
    assert cavern.totalFlashes() == 204
    assert cavern.getEnergyLevel(0, 0) == 0  # top left
    assert cavern.getEnergyLevel(-1, -1) == 0  # bottom right

    for step in range(11, 101):
        cavern.step()  # steps 11 to 100
    assert cavern.totalFlashes() == 1656
    assert cavern.getEnergyLevel(0, 0) == 0  # top left
    assert cavern.getEnergyLevel(-1, -1) == 6  # bottom right
