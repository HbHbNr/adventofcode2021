from typing import List, Tuple, Dict, Set
import math


class Polymer:

    def __init__(self, lines: List[str]) -> None:
        self._symbolMap, self._numberMap = Polymer.createSymbolMaps(lines)
        print(self._symbolMap)
        print(self._numberMap)
        self._template = [self.lookupSymbol(char) for char in lines[0]]
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
        print(self._histogram)

    def lookupSymbol(self, symbol: str) -> int:
        return self._symbolMap[symbol]

    def lookupNumber(self, number: int) -> str:
        return self._numberMap[number]

    @classmethod
    def preheatHistogram(cls, symbolCount, template) -> Dict[int, int]:
        histogram: Dict[int, int] = dict()
        for number in range(symbolCount):
            histogram[number] = 0
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

    def histogram(self) -> Dict[int, int]:
        return self._histogram

    def __str__(self):
        return self._template


if __name__ == '__main__':
    from days import util
    import sys

    lines = util.readinputfile('inputfiles/day14_example.txt')
    # lines = util.readinputfile('inputfiles/day14_input.txt')
    polymer = Polymer(lines)
    number = 20
    profile = len(sys.argv) > 1  # add any parameter to activate profiling
    if profile:
        import cProfile
        cProfile.run('polymer.steps(number)')
    else:
        polymer.steps(number)
    histogram = polymer.histogram()
    # print(histogram)
    values = list(histogram.values())
    values.sort()
    diff = values[-1] - values[0]

    util.printresultline(f'14b ({number} steps!)', diff)
