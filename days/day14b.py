from typing import List, Tuple, Dict, Set
import math


class Polymer:

    def __init__(self, lines: List[str]) -> None:
        self._symbolMap, self._numberMap = Polymer.createSymbolMaps(lines)
        print(self._symbolMap)
        print(self._numberMap)
        self._template: List[int] = [self.lookupSymbol(char) for char in lines[0]]
        print(self._template)
        self._shiftKey = int.bit_length(len(self._symbolMap) - 1)
        print(self._shiftKey)

        # create rules
        self._rules: List[int] = [0] * int(math.pow(2, 2 * self._shiftKey))
        # print(self._rules)
        print(len(self._rules))
        for line in lines[2:]:
            a = self.lookupSymbol(line[0])
            b = self.lookupSymbol(line[1])
            key = a << self._shiftKey | b
            value = self.lookupSymbol(line[6])
            # print(str(self._rules) + ' ' + str(key) + ' ' + str(value))
            self._rules[key] = value
        # print(self._rules)

        # prepare histogram with all possible symbols
        self._histogram = Polymer.preheatHistogram(len(self._symbolMap), self._template)
        self._histogramLen = len(self._histogram)
        print(self._histogram)

        self._cache: Dict[Tuple[int, int], List[int]] = dict()

    def lookupSymbol(self, symbol: str) -> int:
        return self._symbolMap[symbol]

    def lookupNumber(self, number: int) -> str:
        return self._numberMap[number]

    @classmethod
    def preheatHistogram(cls, symbolCount, template) -> List[int]:
        histogram: List[int] = [0] * symbolCount
        for number in template:
            histogram[number] += 1
        # print(f'found {len(histogram)} symbols: {",".join(histogram.keys())}')
        return histogram

    @classmethod
    def createSymbolMaps(cls, lines: List[str]) -> Tuple[Dict[str, int], Dict[int, str]]:
        symbols: Set[str] = set(lines[0])
        for line in lines[2:]:
            symbols.add(line[6])
        print(f'found {len(symbols)} symbols: {",".join(symbols)}')

        symbolMap: Dict[str, int] = dict()
        numberMap: Dict[int, str] = dict()
        number = 0
        for symbol in symbols:
            symbolMap[symbol] = number
            numberMap[number] = symbol
            number += 1
        return symbolMap, numberMap

    def steps(self, level: int) -> None:
        # idea 1: switch back to recursive, but keep track of already solved pairs
        # idea 2: multiple rules lead to the same new element
        #         - solved pairs are also valid for other pairs with the same new element
        template: List[Tuple[int, int]] = [(number, level) for number in self._template]
        length = len(template)
        template.extend([(0, 0)] * level)  # reserve space for additional elements
        while length > 0:
            if length > 1:  # examine last two elements
                a = template[length - 2]
                b = template[length - 1]
                a1 = a[1]
                b1 = b[1]
                # (at least) one element is at the lowest level
                if a1 == 0 or b1 == 0:
                    # print(a[0], b[0], sep='', end='')
                    # remove two last elements: just forget about them
                    length -= 2
                # no element is at the lowest level
                else:
                    key = a[0] << self._shiftKey | b[0]
                    c: int = self._rules[key]
                    self._histogram[c] += 1
                    if a1 < b1:
                        template[length - 1] = (c, a1 - 1)
                    else:
                        template[length - 1] = (c, b1 - 1)
                    template[length] = b
                    length += 1
            elif length == 1:  # last element of template
                # print(template[0][0])
                break
        print(self._histogram)

    def steps_recursive(self, level: int) -> None:
        if level > 0:
            for i in range(0, len(self._template) - 1):
                a = self._template[i]
                b = self._template[i + 1]
                histogram = self.step_recursive(level, a, b)
                for i in range(self._histogramLen):
                    self._histogram[i] += histogram[i]
        print(f'cachesize: {len(self._cache)}')

    def step_recursive(self, level: int, a: int, b: int) -> List[int]:
        # look into cache here, only if not found do step_recursive()
        # unclear: when is the content of the cache added to the histogram?
        # the content of the cache should be used *instead* of doing the recursion
        key = a << self._shiftKey | b
        cachekey = (key, level)
        if cachekey in self._cache:
            histogram = self._cache[cachekey]
        else:
            c: int = self._rules[key]
            histogram = [0] * self._histogramLen
            histogram[c] = 1
            if level > 1:
                ah = self.step_recursive(level - 1, a, c)
                bh = self.step_recursive(level - 1, c, b)
                for i in range(self._histogramLen):
                    histogram[i] += ah[i] + bh[i]
            self._cache[cachekey] = histogram
        return histogram
        # make step_recursive return the histogram and save it to the cache

    def histogram(self) -> Dict[str, int]:
        histogram: Dict[str, int] = dict([(self.lookupNumber(i), self._histogram[i]) for i in range(len(self._histogram))])
        return histogram

    def __str__(self):
        return self._template


if __name__ == '__main__':
    from days import util
    import sys

    # lines = util.readinputfile('inputfiles/day14_example.txt')
    lines = util.readinputfile('inputfiles/day14_input.txt')
    polymer = Polymer(lines)
    number = 40
    profile = len(sys.argv) > 1  # add any parameter to activate profiling
    if profile:
        import cProfile
        cProfile.run('polymer.steps_recursive(number)')
    else:
        polymer.steps_recursive(number)
    histogram = polymer.histogram()
    print(histogram)
    values = list(histogram.values())
    values.sort()
    diff = values[-1] - values[0]

    util.printresultline(f'14b ({number} steps!)', diff)
