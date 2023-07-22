"""Solution for https://adventofcode.com/2021/day/14 part b"""
from typing import List, Tuple, Dict, Set
import math
from util import util


class Polymer:
    # pylint: disable=too-many-instance-attributes

    def __init__(self, lines: List[str]) -> None:
        # create mapping between symbols and numbers
        self._symbolMap, self._numberMap = Polymer.createSymbolMaps(lines)
        # print(self._symbolMap)
        # print(self._numberMap)

        # translate template from symbols to numbers
        self._template: List[int] = [self.lookupSymbol(char) for char in lines[0]]
        # print(list(lines[0]))
        # print(self._template)

        # determine how many bits the first part of the rule head must be moved left
        self._shiftKey = int.bit_length(len(self._symbolMap) - 1)
        # print(self._shiftKey)

        # create rules
        self._rules: List[int] = [0] * int(math.pow(2, 2 * self._shiftKey))
        for line in lines[2:]:
            left = self.lookupSymbol(line[0])
            right = self.lookupSymbol(line[1])
            key = left << self._shiftKey | right
            middle = self.lookupSymbol(line[6])
            self._rules[key] = middle
        # print(self._rules)

        # prepare histogram with all possible symbols
        self._histogram = Polymer.preheatHistogram(len(self._symbolMap), self._template)
        self._histogramLen = len(self._histogram)
        # print(self._histogram)

        self._cache: Dict[Tuple[int, int], List[int]] = {}

    def lookupSymbol(self, symbol: str) -> int:
        return self._symbolMap[symbol]

    def lookupNumber(self, number: int) -> str:
        return self._numberMap[number]

    @classmethod
    def preheatHistogram(cls, symbolCount, template) -> List[int]:
        histogram: List[int] = [0] * symbolCount
        for number in template:
            histogram[number] += 1
        return histogram

    @classmethod
    def createSymbolMaps(cls, lines: List[str]) -> Tuple[Dict[str, int], Dict[int, str]]:
        symbols: Set[str] = set(lines[0])
        for line in lines[2:]:
            symbols.add(line[6])
        # print(f'found {len(symbols)} symbols: {",".join(symbols)}')
        symbolMap: Dict[str, int] = {}
        numberMap: Dict[int, str] = {}
        number = 0
        for symbol in symbols:
            symbolMap[symbol] = number
            numberMap[number] = symbol
            number += 1
        return symbolMap, numberMap

    def stepsRecursive(self, level: int) -> None:
        if level > 0:
            for i in range(0, len(self._template) - 1):
                left = self._template[i]
                right = self._template[i + 1]
                histogram = self.stepRecursive(level, left, right)
                for i in range(self._histogramLen):
                    self._histogram[i] += histogram[i]
        # print(f'final cachesize: {len(self._cache)}')

    def stepRecursive(self, level: int, left: int, right: int) -> List[int]:
        key = left << self._shiftKey | right
        cachekey = (key, level)
        if cachekey in self._cache:
            histogram = self._cache[cachekey]
        else:
            middle: int = self._rules[key]
            histogram = [0] * self._histogramLen
            histogram[middle] = 1
            if level > 1:
                leftHistogram = self.stepRecursive(level - 1, left, middle)
                rightHistogram = self.stepRecursive(level - 1, middle, right)
                for i in range(self._histogramLen):
                    histogram[i] += leftHistogram[i] + rightHistogram[i]
            self._cache[cachekey] = histogram
        return histogram

    def histogram(self) -> Dict[str, int]:
        histogram: Dict[str, int] = dict((self.lookupNumber(i), self._histogram[i]) for i in range(len(self._histogram)))
        return histogram

    def __str__(self):
        return self._template


def main():
    # lines = util.readinputfile('inputfiles/day14_example.txt')
    lines = util.readinputfile('inputfiles/day14_input.txt')
    polymer = Polymer(lines)
    number = 40
    # profile = len(sys.argv) > 1  # add any parameter to activate profiling
    # if profile:
    #     import cProfile
    #     cProfile.run('polymer.stepsRecursive(number)')
    # else:
    #     polymer.stepsRecursive(number)
    polymer.stepsRecursive(number)
    histogram = polymer.histogram()
    # print(histogram)
    values = list(histogram.values())
    values.sort()
    diff = values[-1] - values[0]

    util.printresultline('14b', diff)


if __name__ == '__main__':
    main()
