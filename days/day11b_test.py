from util import util
from days import day11b


def testExample():
    lines = util.readinputfile('inputfiles/day11_example.txt')
    cavern = day11b.Cavern(lines)

    # note: all coordinates must respect the additional frame of 0s

    assert cavern.getTotalFlashes() == 0
    assert cavern.getEnergyLevel(1, 1) == 5  # top left
    assert cavern.getEnergyLevel(-2, -2) == 6  # bottom right

    firstFlashAt = 195

    for step in range(1, firstFlashAt + 1):
        allFlashed = cavern.step()  # steps 1 to <firstFlashAt>
        if allFlashed:
            assert step == firstFlashAt  # only in step <firstFlashAt> they all flash
        else:
            assert step != firstFlashAt  # in all other steps never all flash


def testInput():
    lines = util.readinputfile('inputfiles/day11_input.txt')
    cavern = day11b.Cavern(lines)

    firstFlashAt = 346

    for step in range(1, firstFlashAt + 1):
        allFlashed = cavern.step()  # steps 1 to <firstFlashAt>
        if allFlashed:
            assert step == firstFlashAt  # only in step <firstFlashAt> they all flash
        else:
            assert step != firstFlashAt  # in all other steps never all flash
