from typing import List, Tuple


class Matrix:

    def __init__(self, lines: List[str]) -> None:
        self._dots = set()
        self._maxx = 0
        self._maxy = 0

        emptyline = lines.index('')
        folddir, foldnum = Matrix.splitFoldCommand(lines[emptyline + 1])

        lines2 = iter(lines)
        line = next(lines2)
        while line != '':
            xstr, ystr = line.split(',')
            x = int(xstr)
            y = int(ystr)

            x, y = Matrix.folddot(folddir, foldnum, x, y)

            self._maxx = max(self._maxx, x)
            self._maxy = max(self._maxy, y)
            self._dots.add((x, y))
            line = next(lines2)

    def fold(self, steps) -> None:
        pass

    def countDots(self) -> int:
        return len(self._dots)

    @classmethod
    def folddot(cls, folddir, foldnum, x, y) -> Tuple[int, int]:
        if folddir == 'x' and x > foldnum:
            x = foldnum - (x - foldnum)
            pass
        elif folddir == 'y' and y > foldnum:
            y = foldnum - (y - foldnum)
            pass
        return (x, y)

    @classmethod
    def splitFoldCommand(cls, line: str) -> Tuple[str, int]:
        _, _, line = line.split(' ')
        dir, numstr = line.split('=')
        num = int(numstr)
        return dir, num

    def __str__(self):
        return str(self._maxx) + 'x' + str(self._maxy)


if __name__ == '__main__':
    from days import util

    # lines = util.readinputfile('inputfiles/day13_example.txt')
    lines = util.readinputfile('inputfiles/day13_input.txt')
    matrix = Matrix(lines)
    # print(matrix)
    matrix.fold(1)

    print('DAY13A: ' + str(matrix.countDots()))
