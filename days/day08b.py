"""Solution for https://adventofcode.com/2021/day/8 part b"""
from util import util


# steps to determine all numbers
# distinct string lengths: 1, 7, 8, 8
# (7 - 1 -> a)
# 6c contains 4 -> 9, rest: 6c2
# 6c2 contains 1 -> 0, rest: 6
# (8 - 9 -> e)
# (8 - 0 -> d)
# (8 - 6 -> c)
# 5c contained in 6 -> 5, rest: 5c2
# 5c2 contains 1 -> 3, rest: 2

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
    def isdictinctstring(cls, string):
        return cls.isdictinctnumberofchars(len(string))

    @classmethod
    def isdictinctnumberofchars(cls, numberofchars):
        return len(cls.numberofcharstodigits(numberofchars)) == 1


class Pattern:
    def __init__(self, string):
        self._string = tuple(string)
        self._chars = frozenset(string)

    def __str__(self):
        return str(self._chars)

    def __repr__(self):
        return repr(self._chars)

    def string(self):
        return str(''.join(self._string))

    def chars(self):
        return self._chars


class PatternMap:
    def __init__(self, patternstrings):
        self._patternmap = PatternMap._evaluate(patternstrings)

    @staticmethod
    def _evaluate(patternstrings):
        patternmap = {}
        g5c = []
        g6c = []
        for patternstring in patternstrings:
            digits = DigitMap.numberofcharstodigits(len(patternstring))
            pattern = Pattern(patternstring)
            sortedpatternstring = ''.join(sorted(patternstring))
            if len(digits) == 1:
                digit = digits[0]
                patternmap[sortedpatternstring] = digit
                patternmap[digit] = pattern
            elif len(patternstring) == 5:
                g5c.append(pattern)
            elif len(patternstring) == 6:
                g6c.append(pattern)
        PatternMap._evaluateg6c(patternmap, g6c)
        PatternMap._evaluateg5c(patternmap, g5c)
        return patternmap

    @staticmethod
    def _evaluateg6c(patternmap, g6c):
        for pattern in g6c:
            sortedpatternstring = ''.join(sorted(pattern.string()))
            # 6c contains 4 -> 9, rest: 6c2
            if pattern.chars().issuperset(patternmap[4].chars()):
                patternmap[sortedpatternstring] = 9
                patternmap[9] = pattern
            # 6c2 contains 1 -> 0, rest: 6
            elif pattern.chars().issuperset(patternmap[1].chars()):
                patternmap[sortedpatternstring] = 0
                patternmap[0] = pattern
            # 6
            else:
                patternmap[sortedpatternstring] = 6
                patternmap[6] = pattern

    @staticmethod
    def _evaluateg5c(patternmap, g5c):
        for pattern in g5c:
            sortedpatternstring = ''.join(sorted(pattern.string()))
            # 5c contained in 6 -> 5, rest: 5c2
            if pattern.chars().issubset(patternmap[6].chars()):
                patternmap[sortedpatternstring] = 5
                patternmap[5] = pattern
            # 5c2 contains 1 -> 3, rest: 2
            elif pattern.chars().issuperset(patternmap[1].chars()):
                patternmap[sortedpatternstring] = 3
                patternmap[3] = pattern
            # 2
            else:
                patternmap[sortedpatternstring] = 2
                patternmap[2] = pattern

    def __str__(self):
        return str(self._patternmap)

    def lookuppatternstring(self, patternstring):
        sortedpatternstring = ''.join(sorted(patternstring))
        # print(sortedpatternstring)
        for key, value in self._patternmap.items():
            # print(k)
            if key == sortedpatternstring:
                # print(f'{k} does match')
                # print(v)
                # print()
                return value
            # else:
                # print(f'{k} does not match')
        # print()
        return None


class Panel:
    def __init__(self, line):
        parts = line.split(' ')
        patternstrings = parts[0:10]
        self._patternmap = PatternMap(patternstrings)
        # print(self._patternmap)
        self._outputs = parts[11:]

    def countdistinctdigits(self):
        count = 0
        for output in self._outputs:
            if DigitMap.isdictinctstring(output):
                count += 1
        return count

    @staticmethod
    def countalldistinctdigits(lines):
        totalcount = 0
        for line in lines:
            panel = Panel(line)
            totalcount += panel.countdistinctdigits()
        return totalcount

    def output(self):
        # print(self._outputs)
        digits = 0
        for output in self._outputs:
            digits *= 10
            digits += self._patternmap.lookuppatternstring(output)
        # print(digits)
        return digits

    @staticmethod
    def sumoutputs(lines):
        totalsum = 0
        for line in lines:
            panel = Panel(line)
            totalsum += panel.output()
        return totalsum


def main():
    # lines = util.readinputfile('inputfiles/day08_example.txt')
    lines = util.readinputfile('inputfiles/day08_input.txt')
    totalsum = Panel.sumoutputs(lines)

    util.printresultline('8b', totalsum)


if __name__ == '__main__':
    main()
