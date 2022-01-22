from math import copysign
import re


class Map:
    _linepattern = re.compile(r"^(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)$")

    def __init__(self, lines):
        xmax = 0
        ymax = 0
        for line in lines:
            match = self._linepattern.match(line)
            # print(match.group(0))
            # print(match.group('x1'))
            # print(match.group('y1'))
            # print(match.group('x2'))
            # print(match.group('y2'))
            xmax = max(xmax, int(match.group('x1')), int(match.group('x2')))
            ymax = max(ymax, int(match.group('y1')), int(match.group('y2')))
        # print(f'xmax={xmax} ymax={ymax}')
        self._width = xmax + 1
        self._height = ymax + 1
        self._coords = [[0 for y in range(self._height)] for x in range(self._width)]
        for line in lines:
            match = self._linepattern.match(line)
            # x1 = match.group('x1')
            # y1 = match.group('y1')
            # x2 = match.group('x2')
            # y2 = match.group('y2')
            self.drawline(int(match.group('x1')), int(match.group('y1')), int(match.group('x2')), int(match.group('y2')))

    def drawline(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    self._coords[x][y] += 1

    def print(self):
        for y in range(self._height):
            for x in range(self._width):
                print(self._coords[x][y], end='')
            print()

    def size(self):
        return {'width': self._width, 'height': self._height}


if __name__ == '__main__':
    import util

    lines = util.readinputfile('inputfiles/day5_example.txt')
    # lines = util.readinputfile('inputfiles/day5_input.txt')
    map = Map(lines)
    print(map.size())
    map.print()
