from typing import List


class Heightmap:

    def __init__(self, lines: List[str]) -> None:
        self._maxx = len(lines[0])
        self._maxy = len(lines)
        self._rows = []
        self._rows.append('9' * (1 + self._maxx + 1))
        for line in lines:
            row = '9' + line + '9'
            self._rows.append(row)
        self._rows.append('9' * (1 + self._maxx + 1))

    def findlowpoints(self) -> List[int]:
        lowpoints = []
        for y in range(1, self._maxy + 1):
            for x in range(1, self._maxx + 1):
                height = int(self._rows[y][x])
                if height < int(self._rows[y-1][x]):
                    if height < int(self._rows[y+1][x]):
                        if height < int(self._rows[y][x-1]):
                            if height < int(self._rows[y][x+1]):
                                lowpoints.append(height)
        return lowpoints

    def calcrisklevel(self) -> int:
        lowpoints = self.findlowpoints()
        risklevel = sum(lowpoints) + len(lowpoints)
        return risklevel

    def print(self) -> None:
        for row in self._rows:
            print(row)


if __name__ == '__main__':
    from days import util

    # lines = util.readinputfile('inputfiles/day9_example.txt')
    lines = util.readinputfile('inputfiles/day9_input.txt')
    heightmap = Heightmap(lines)
    # heightmap.print()

    # print("lowPoints: " + str(heightmap.findlowpoints()))
    print("riskLevel: " + str(heightmap.calcrisklevel()))
