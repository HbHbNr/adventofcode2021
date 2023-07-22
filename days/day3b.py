"""Solution for https://adventofcode.com/2021/day/3 part b"""
import fileinput
from util import util


class Histogram:
    def __init__(self):
        self.frequencies = {'0': 0, '1': 0}

    def add(self, value):
        self.frequencies[value] += 1

    def comparevalues(self, mostcommon):
        value = '1' if mostcommon else '0'
        diff = self.frequencies['0'] - self.frequencies['1']
        diff = diff if mostcommon else -diff
        if diff != 0:
            value = '0' if diff > 0 else '1'
        return value


def createhistogram(lines, index):
    histogram = Histogram()
    for line in lines:
        value = line[index]
        histogram.add(value)
    return histogram


def readinputfile(inputfile):
    lines = []
    for line in fileinput.input(inputfile):
        lines.append(line.rstrip())
    return lines


def filterlines(lines, mostcommon):
    maxindex = len(lines[0])
    for index in range(maxindex):
        histogram = createhistogram(lines, index)
        value = histogram.comparevalues(mostcommon)
        lines2 = list(filter(lambda line: line[index] == value, lines))  # pylint: disable=cell-var-from-loop
        lines = lines2
        if len(lines) == 1:
            break
    return lines[0]


def determineratings(inputfile):
    lines = readinputfile(inputfile)
    oxygen = filterlines(lines.copy(), True)
    co2 = filterlines(lines.copy(), False)
    return (oxygen, co2)


def main():
    oxygen, co2 = determineratings('inputfiles/day3_input.txt')
    # print('oxygen: {} -> {}'.format(oxygen, int(oxygen, 2)))
    # print('co2: {} -> {}'.format(co2, int(co2, 2)))
    # print('oxygen * co2: {}'.format(int(oxygen, 2) * int(co2, 2)))

    util.printresultline('3b', int(oxygen, 2) * int(co2, 2))


if __name__ == '__main__':
    main()
