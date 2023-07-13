from util import util
from days import day11b


def test_example():
    lines = util.readinputfile('inputfiles/day11_example.txt')
    cavern = day11b.Cavern(lines)

    # note: all coordinates must respect the additional frame of 0s

    assert cavern.getTotalFlashes() == 0
    assert cavern.getEnergyLevel(1, 1) == 5  # top left
    assert cavern.getEnergyLevel(-2, -2) == 6  # bottom right

    FIRST_FLASH = 195

    for step in range(1, FIRST_FLASH + 1):
        allFlashed = cavern.step()  # steps 1 to <firstflash>
        if allFlashed:
            assert step == FIRST_FLASH  # only in step <firstflash> they all flash
        else:
            assert step != FIRST_FLASH  # in all other steps never all flash


def test_input():
    lines = util.readinputfile('inputfiles/day11_input.txt')
    cavern = day11b.Cavern(lines)

    FIRST_FLASH = 346

    for step in range(1, FIRST_FLASH + 1):
        allFlashed = cavern.step()  # steps 1 to <firstflash>
        if allFlashed:
            assert step == FIRST_FLASH  # only in step <firstflash> they all flash
        else:
            assert step != FIRST_FLASH  # in all other steps never all flash
