"""Solution for https://adventofcode.com/2021/day/3 part a"""
import fileinput
from util import util


class Histogram:
    def __init__(self, maxindex):
        self.frequencies = [{'0': 0, '1': 0} for x in range(maxindex)]

    def add(self, index, value):
        self.frequencies[index][value] += 1

    def buildparameter(self, mostcommon):
        parameter = []
        for _, values in enumerate(self.frequencies):
            # print(values)
            diff = values['0'] - values['1']
            diff = diff if mostcommon else -diff
            parameter.append('0' if diff > 0 else '1')
        return ''.join(parameter)


def createhistogram(inputfile):
    histogram = None
    for line in fileinput.input(inputfile):
        line = line.rstrip()
        if fileinput.lineno() == 1:
            histogram = Histogram(len(line))
        for index, value in enumerate(line):
            histogram.add(index, value)
    return histogram


def main():
    # inputfile = "inputfiles/day3_example.txt"
    inputfile = "inputfiles/day3_input.txt"

    histogram = createhistogram(inputfile)
    # print(histogram.frequencies)
    gamma = histogram.buildparameter(True)
    epsilon = histogram.buildparameter(False)
    # print('gamma: {} -> {}'.format(gamma, int(gamma, 2)))
    # print('epsilon: {} -> {}'.format(epsilon, int(epsilon, 2)))
    # print('gamma * epsilon: {}'.format(int(gamma, 2) * int(epsilon, 2)))

    util.printresultline('3a', int(gamma, 2) * int(epsilon, 2))


if __name__ == '__main__':
    main()
