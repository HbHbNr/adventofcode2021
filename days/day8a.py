class DigitMap:
    # map number of chars to possible digit(s)
    # 2c -> 1
    # 3c -> 7
    # 4c -> 4
    # 5c -> 2, 3, 5
    # 6c -> 0, 6, 9
    # 7c -> 8
    _mapnumberofcharstodigits = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}

    @classmethod
    def numberofcharstodigits(cls, numberofchars):
        return cls._mapnumberofcharstodigits[numberofchars]

    @classmethod
    def isdictinctnumberofchars(cls, numberofchars):
        return len(cls.numberofcharstodigits(numberofchars)) == 1


class Panel:
    def __init__(self, line):
        parts = line.split(' ')
        self._patterns = parts[0:10]
        self._outputs = parts[11:]

    def countdistinctdigits(self):
        count = 0
        for output in self._outputs:
            if DigitMap.isdictinctnumberofchars(len(output)):
                count += 1
        return count

    @staticmethod
    def countalldistinctdigits(lines):
        totalcount = 0
        for line in lines:
            panel = Panel(line)
            totalcount += panel.countdistinctdigits()
        return totalcount


def main():
    from util import util

    # lines = util.readinputfile('inputfiles/day8_example.txt')
    lines = util.readinputfile('inputfiles/day8_input.txt')
    totalcount = Panel.countalldistinctdigits(lines)
    print(f'totalcount: {totalcount}')


if __name__ == '__main__':
    main()
