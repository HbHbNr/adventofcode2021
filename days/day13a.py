from typing import List, Dict, Set


class Matrix:

    def __init__(self, lines: List[str]) -> None:
        self._dots = set()
        self._maxx = 0
        self._maxy = 0

        lines2 = iter(lines)
        line = next(lines2)
        while line != '':
            x, y = line.split(',')
            x = int(x)
            y = int(y)
            self._maxx = max(self._maxx, x)
            self._maxy = max(self._maxy, y)
            self._dots.add((x, y))
            line = next(lines2)

    def fold(self, steps) -> None:
        pass

    def countDots(self) -> int:
        return len(self._dots)

    def __str__(self):
        return str(self._maxx) + 'x' + str(self._maxy)


if __name__ == '__main__':
    from days import util

    # lines = util.readinputfile('inputfiles/day13_example.txt')
    lines = util.readinputfile('inputfiles/day13_input.txt')
    matrix = Matrix(lines)
    print(matrix)
    matrix.fold(1)

    print('DAY13A: ' + str(matrix.countDots()))
