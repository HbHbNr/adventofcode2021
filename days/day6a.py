"""Solution for https://adventofcode.com/2021/day/6 part a"""
from util import util


class School:
    def __init__(self, line):
        self._fishes = [int(x) for x in line.split(',')]
        # self._startfishes = tuple(self._fishes)

    def __str__(self):
        return str(self._fishes)

    def size(self):
        return len(self._fishes)

    def nextday(self):
        nextfishes = []
        newfishes = []
        for fish in self._fishes:
            if fish > 0:
                nextfishes.append(fish - 1)
            else:
                nextfishes.append(6)
                newfishes.append(8)
        self._fishes = nextfishes + newfishes

    def nextdays(self, days, progress=False):
        for day in range(1, days + 1):
            if progress:
                print(f'Day {day}')
            self.nextday()

    def getFishes(self):
        return tuple(self._fishes)


def main():
    # lines = util.readinputfile('inputfiles/day6_example.txt')
    lines = util.readinputfile('inputfiles/day6_input.txt')
    school = School(lines[0])
    # print(school.size())
    # print(school)
    school.nextdays(80, False)
    # print(school.size())
    # print(school)
    util.printresultline('6a', school.size())


if __name__ == '__main__':
    main()
