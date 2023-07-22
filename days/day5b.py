"""Solution for https://adventofcode.com/2021/day/5 part b"""
from math import copysign
import re
from util import util


class Map:
    _linepattern = re.compile(r"^(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)$")

    def __init__(self, lines):
        xmax = 0
        ymax = 0
        for line in lines:
            match = self._linepattern.match(line)
            xmax = max(xmax, int(match.group('x1')), int(match.group('x2')))
            ymax = max(ymax, int(match.group('y1')), int(match.group('y2')))
        self._width = xmax + 1
        self._height = ymax + 1
        self._coords = [[0 for y in range(self._height)] for x in range(self._width)]
        for line in lines:
            match = self._linepattern.match(line)
            self.drawlinehv(int(match.group('x1')), int(match.group('y1')), int(match.group('x2')), int(match.group('y2')))

    def drawlinehv(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    self._coords[x][y] += 1
        else:
            self.drawlined(x1, y1, x2, y2)

    def drawlined(self, x1, y1, x2, y2):
        if x2 < x1:
            # pylint: disable=arguments-out-of-order
            # always draw from left to right
            self.drawlined(x2, y2, x1, y1)
        else:
            # check if direction is up or down
            ystep = int(copysign(1, y2 - y1))

            y = y1
            for x in range(x1, x2 + 1):
                self._coords[x][y] += 1
                y += ystep

    def countdangerouscoords(self):
        count = 0
        for y in range(self._height):
            for x in range(self._width):
                if self._coords[x][y] >= 2:
                    count += 1
        return count

    def __str__(self):
        string = ''
        for y in range(self._height):
            string += '' if len(string) == 0 else '\n'
            for x in range(self._width):
                string += str(self._coords[x][y])
        return string

    def size(self):
        return {'width': self._width, 'height': self._height}

    # for unit testing
    def testCoord(self, x, y, value) -> bool:
        return self._coords[x][y] == value


def main():
    # lines = util.readinputfile('inputfiles/day5_example.txt')
    lines = util.readinputfile('inputfiles/day5_input.txt')
    theMap = Map(lines)
    # print(theMap.size())
    # print(map)
    util.printresultline('5b', theMap.countdangerouscoords())


if __name__ == '__main__':
    main()
