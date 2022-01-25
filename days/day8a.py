# map number of chars to possible digit(s)
# 2c -> 1
# 3c -> 7
# 4c -> 4
# 5c -> 2, 3, 5
# 6c -> 0, 6, 9
# 7c -> 8

# steps to determine all numbers
# 7 - 1 -> a
# 6c contains 4 -> 9, rest: 6c2
# 6c2 contains 1 -> 0, rest: 6
# 8 - 9 -> e
# (8 - 0 -> d)
# (8 - 6 -> c)
# 6 - e -> 5  or without intermediate step:  6 - (8 - 9) -> 5
# 5c remove 5 -> 5c2
# 5c2 contains 1 -> 3, rest: 2

class DigitMap:
    def __init__(self):
        self._mapnumberofcharstodigits = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}

    def __getitem__(self, numberofchars):
        return self._mapnumberofcharstodigits[numberofchars]


class Panel:
    def __init__(self, digitmap, line):
        self._digitmap = digitmap
        self._parts = line.split(' ')

    def countdistinctdigits(self):
        count = 0
        # print(self._parts)
        for part in self._parts[11:]:
            # print(part)
            # print(len(part))
            if len(self._digitmap[len(part)]) == 1:
                count += 1
        return count


if __name__ == '__main__':
    import util

    # lines = util.readinputfile('inputfiles/day8_example.txt')
    lines = util.readinputfile('inputfiles/day8_input.txt')
    digitmap = DigitMap()
    totalcount = 0
    for line in lines:
        panel = Panel(digitmap, line)
        totalcount += panel.countdistinctdigits()
    print(totalcount)
