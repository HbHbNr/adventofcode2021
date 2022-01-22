import re


class Map:
    _linepattern = re.compile(r"^(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)$")

    def __init__(self, lines):
        xmax = 0
        ymax = 0
        for line in lines:
            match = self._linepattern.match(line)
            # print(m.group(0))
            # print(m.group('x1'))
            # print(m.group('y1'))
            # print(m.group('x2'))
            # print(m.group('y2'))
            xmax = max(xmax, int(match.group('x1')), int(match.group('x2')))
            ymax = max(ymax, int(match.group('y1')), int(match.group('y2')))
        # print(f'xmax={xmax} ymax={ymax}')
        self._width = xmax + 1
        self._height = ymax + 1
        self._coords = [[0 for y in range(self._height)] for x in range(self._width)]

    def print(self):
        for x in range(self._width):
            for y in range(self._height):
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
