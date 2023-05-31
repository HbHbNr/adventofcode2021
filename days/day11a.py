from typing import List


class Cavern:

    def __init__(self, lines: List[str]) -> None:
        # TODO: add a frame of 0s
        self._maxx = len(lines[0])
        self._maxy = len(lines)
        self._rows = []
        for line in lines:
            self._rows.append([int(energylevel) for energylevel in line])
        self._totalFlashes = 0
        return

    def step(self) -> None:
        self.incrementAll()
        # while at least one 9 exists:
        # - search for first 9
        # - increase it to 10
        # - increase adjacent by 1, but not over 9
        # - repeat
        # reset all 10s to 0
        # reset frame to 0s

    def incrementAll(self) -> None:
        for y in range(0, self._maxy):
            for x in range(0, self._maxx):
                self._rows[y][x] += 1

    def totalFlashes(self) -> int:
        return self._totalFlashes

    def getEnergyLevel(self, x, y) -> int:
        return self._rows[y][x]

    def __str__(self):
        lines = []
        for row in self._rows:
            lines.append(''.join([str(energylevel) for energylevel in row]))
        return '\n'.join(lines)


if __name__ == '__main__':
    from days import util

    lines = util.readinputfile('inputfiles/day11_example.txt')
    # lines = util.readinputfile('inputfiles/day11_input.txt')
    cavern = Cavern(lines)
    print(cavern)
    cavern.step()
    print(cavern)
