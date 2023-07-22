"""Solution for https://adventofcode.com/2021/day/13 part b"""
from typing import List, Tuple, Set
from util import util


class Matrix:
    _dotmark = '#'
    _nodotmark = '.'

    def __init__(self, lines: List[str]) -> None:
        self._dots: Set[Tuple[int, int]] = set()
        self._foldcommands: List[Tuple[str, int]] = []

        emptyline = lines.index('')

        for line in lines[:emptyline]:
            xstr, ystr = line.split(',')
            x = int(xstr)
            y = int(ystr)
            self._dots.add((x, y))

        for line in lines[emptyline + 1:]:
            folddir, foldnum = Matrix.splitFoldCommand(line)
            self._foldcommands.append((folddir, foldnum))

    def fold(self):
        for folddir, foldnum in self._foldcommands:
            fixdots = set()
            for dot in self._dots:
                fixdots.add(Matrix.folddot(folddir, foldnum, dot[0], dot[1]))
            self._dots = fixdots

    def findMax(self) -> Tuple[int, int]:
        maxx: int = 0
        maxy: int = 0
        for dot in self._dots:
            maxx = max(maxx, dot[0])
            maxy = max(maxy, dot[1])
        return (maxx, maxy)

    def countDots(self) -> int:
        return len(self._dots)

    @classmethod
    def folddot(cls, folddir, foldnum, x, y) -> Tuple[int, int]:
        if folddir == 'x' and x > foldnum:
            x = foldnum - (x - foldnum)
        elif folddir == 'y' and y > foldnum:
            y = foldnum - (y - foldnum)
        return (x, y)

    @classmethod
    def splitFoldCommand(cls, line: str) -> Tuple[str, int]:
        _, _, line = line.split(' ')
        folddir, foldnumstr = line.split('=')
        foldnum = int(foldnumstr)
        return folddir, foldnum

    def __str__(self):
        maxx, maxy = self.findMax()
        lines = []
        for y in range(0, maxy + 1):
            dots = []
            for x in range(0, maxx + 1):
                if (x, y) in self._dots:
                    dots.append(Matrix._dotmark)
                else:
                    dots.append(Matrix._nodotmark)
            lines.append(''.join(dots))
        return '\n'.join(lines)
        # return str(self._foldcommands)


def main():
    # lines = util.readinputfile('inputfiles/day13_example.txt')
    lines = util.readinputfile('inputfiles/day13_input.txt')
    matrix = Matrix(lines)
    # print(matrix)
    matrix.fold()
    # print(matrix)

    util.printresultline('13b', '\n' + str(matrix))


if __name__ == '__main__':
    main()
