from typing import List, Tuple, Set


class Matrix:
    _dotmark = '#'
    _nodotmark = '.'

    def __init__(self, lines: List[str]) -> None:
        self._dots: Set[Tuple[int, int]] = set()
        self._maxx = 0
        self._maxy = 0

        emptyline = lines.index('')
        folddir, foldnum = Matrix.splitFoldCommand(lines[emptyline + 1])

        for line in lines[:emptyline]:
            xstr, ystr = line.split(',')
            x = int(xstr)
            y = int(ystr)

            x, y = Matrix.folddot(folddir, foldnum, x, y)

            self._maxx = max(self._maxx, x)
            self._maxy = max(self._maxy, y)
            self._dots.add((x, y))

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
        lines = []
        for y in range(0, self._maxy + 1):
            dots = []
            for x in range(0, self._maxx + 1):
                if (x, y) in self._dots:
                    dots.append(Matrix._dotmark)
                else:
                    dots.append(Matrix._nodotmark)
            lines.append(''.join(dots))
        return '\n'.join(lines)


if __name__ == '__main__':
    from days import util

    lines = util.readinputfile('inputfiles/day13_example.txt')
    # lines = util.readinputfile('inputfiles/day13_input.txt')
    matrix = Matrix(lines)
    # print(matrix)

    util.printresultline('13a', matrix.countDots())
