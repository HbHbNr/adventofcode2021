from typing import List, Any
from re import sub
from util import util


class Heightmap:

    def __init__(self, lines: List[str]) -> None:
        self._maxx = len(lines[0])
        self._maxy = len(lines)
        self._rows = []
        self._rows.append(['9'] * (1 + self._maxx + 1))
        for line in lines:
            row = ['9']
            row.extend(list(sub(r'[^9]', Heightmap.unknownmarker(), line)))
            row.append('9')
            self._rows.append(row)
        self._rows.append(['9'] * (1 + self._maxx + 1))

    def findbasins(self) -> List[Any]:
        basins = []
        for y in range(1, self._maxy + 1):
            for x in range(1, self._maxx + 1):
                if self.isunknown(x, y):
                    basin = Basin(self, x, y)
                    basins.append(basin)
        sizes = [basin.size() for basin in basins]
        return sorted(sizes, reverse=True)

    def get(self, x, y) -> str:
        return self._rows[y][x]

    def set(self, x, y, marker) -> None:
        self._rows[y][x] = marker

    def isunknown(self, x, y) -> bool:
        return self._rows[y][x] == Heightmap.unknownmarker()

    def print(self) -> None:
        for row in self._rows:
            print(''.join(row))

    @classmethod
    def unknownmarker(cls):
        return ' '


class Basin:
    _markers = [chr(o) for o in range(ord('A'), ord('z') + 1)]

    def __init__(self, heightmap: Heightmap, startx, starty) -> None:
        self._heightmap = heightmap
        self._marker = Basin.popmarker()
        self._size = 0
        self.flowinto(startx, starty)

    def flowinto(self, x, y) -> None:
        if self._heightmap.isunknown(x, y):
            self._heightmap.set(x, y, self._marker)
            self._size += 1

            self.flowinto(x-1, y)
            self.flowinto(x, y+1)
            self.flowinto(x+1, y)
            self.flowinto(x, y-1)

    def size(self) -> int:
        return self._size

    def print(self) -> None:
        print(self._size)

    @classmethod
    def makemarkers(cls) -> List[str]:
        markers = [chr(o) for o in range(ord('A'), ord('Z') + 1)]
        markers.extend([chr(o) for o in range(ord('a'), ord('z') + 1)])
        return markers

    @classmethod
    def popmarker(cls) -> str:
        marker = cls._markers.pop(0)
        cls._markers.append(marker)
        return marker


def main():
    # lines = util.readinputfile('inputfiles/day9_example.txt')
    lines = util.readinputfile('inputfiles/day9_input.txt')
    heightmap = Heightmap(lines)
    # heightmap.print()
    basins = heightmap.findbasins()
    # heightmap.print()
    # print(basins)
    top3product = int(basins[0]) * int(basins[1]) * int(basins[2])

    util.printresultline('9b', top3product)


if __name__ == '__main__':
    main()
