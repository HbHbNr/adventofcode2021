from typing import List


class Cavern:

    def __init__(self, lines: List[str]) -> None:
        # TODO: add a frame of 0s
        self._maxx = len(lines[0])
        self._maxy = len(lines)
        self._rows = []
        self._rows.append([0] * (1 + self._maxx + 1))
        for line in lines:
            row = [0] + [int(energylevel) for energylevel in line] + [0]
            self._rows.append(row)
        self._rows.append([0] * (1 + self._maxx + 1))
        self._totalFlashes = 0

    def step(self) -> None:
        self.incrementAll()

        # while at least one >9 exists:
        # - search for first >9
        # - set it to 0 and increase totalFlashes
        # - increase all adjacent by 1, if not already set to 0
        oneflashed = True
        while oneflashed:
            oneflashed = False
            for y in range(1, self._maxy + 1):
                for x in range(1, self._maxx + 1):
                    energyLevel = self.getEnergyLevel(x, y)
                    if energyLevel > 9:
                        self.flash(x, y)
                        oneflashed = True

    def incrementAll(self) -> None:
        for y in range(1, self._maxy + 1):
            for x in range(1, self._maxx + 1):
                self.incrementEnergyLevel(x, y)

    def flash(self, x, y) -> None:
        for yoffset in range(-1, 2):
            for xoffset in range(-1, 2):
                if yoffset == 0 and xoffset == 0:
                    self.setEnergyLevel(x, y, 0)
                    self._totalFlashes += 1
                else:
                    self.enlighten(x + xoffset, y + yoffset)

    def enlighten(self, x, y) -> None:
        energyLevel = self.getEnergyLevel(x, y)
        if energyLevel == 0:
            pass  # already flashed in this step or is from the frame
        else:
            self.setEnergyLevel(x, y, energyLevel + 1)

    def getTotalFlashes(self) -> int:
        return self._totalFlashes

    def getEnergyLevel(self, x, y) -> int:
        return self._rows[y][x]

    def setEnergyLevel(self, x, y, energyLevel: int) -> None:
        self._rows[y][x] = energyLevel

    def incrementEnergyLevel(self, x, y) -> None:
        self._rows[y][x] += 1

    def __str__(self):
        lines = []
        for row in self._rows:
            lines.append(''.join([str(energylevel) for energylevel in row]))
        return '\n'.join(lines)


if __name__ == '__main__':
    from days import util

    # lines = util.readinputfile('inputfiles/day11_example.txt')
    lines = util.readinputfile('inputfiles/day11_input.txt')
    cavern = Cavern(lines)
    # print(cavern)
    # print(cavern.getTotalFlashes())
    for _ in range(1, 101):
        cavern.step()
    # print(cavern)
    print('DAY11A - Number of total flashes after 100 steps: ' + str(cavern.getTotalFlashes()))
