"""Solution for https://adventofcode.com/2021/day/7 part b"""
from util import util


class Aligner:
    def __init__(self, line):
        self._crabs = tuple(int(crab) for crab in line.split(','))

    def __str__(self):
        return str(self._crabs)

    def size(self):
        return len(self._crabs)

    def calcbestx(self):
        bestx = None
        totalfuels = {}
        for testpos in range(min(self._crabs), max(self._crabs) + 1):
            distances = [abs(testpos - crab) for crab in self._crabs]
            # little Gauss:
            distancecosts = [(distance * (distance + 1)) // 2 for distance in distances]
            totalfuels[testpos] = sum(distancecosts)
            if bestx is None or totalfuels[bestx] > totalfuels[testpos]:
                bestx = testpos

        alignment = {'bestx': bestx, 'totalfuels': totalfuels}
        return alignment


def main():
    # lines = util.readinputfile('inputfiles/day07_example.txt')
    lines = util.readinputfile('inputfiles/day07_input.txt')
    aligner = Aligner(lines[0])
    # print(f'crabs: {aligner.size()}')
    alignment = aligner.calcbestx()
    # # pylint: disable=consider-using-f-string
    # print('bestx: {}  bestfuel: {}'.format(alignment['bestx'], alignment['totalfuels'][alignment['bestx']]))

    util.printresultline('7b', alignment['totalfuels'][alignment['bestx']])


if __name__ == '__main__':
    main()
