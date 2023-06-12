from typing import List, Tuple, Dict


class Polymer:

    def __init__(self, lines: List[str]) -> None:
        self._template = lines[0]

        # create rules
        self._rules: Dict[Tuple[str, str], str] = dict()
        for line in lines[2:]:
            key = line[0], line[1]
            value = line[6]
            self._rules[key] = value

        # prepare histogram with all possible symbols
        histogram: Dict[str, int] = dict()
        for value in self._rules.values():
            histogram[value] = 0
        for char in self._template:
            if char in histogram:
                histogram[char] += 1
            else:
                histogram[char] = 1
        # print(self._template)
        # print(histogram)
        self._histogram = histogram

    def steps(self, number: int) -> None:
        if number > 0:
            for i in range(0, len(self._template) - 1):
                a = self._template[i]
                b = self._template[i + 1]
                self.step(number, a, b)

    def step(self, number: int, a: str, b: str) -> None:
        key = (a, b)
        c = self._rules.get(key)
        if c is not None:
            self._histogram[c] += 1
            if number > 1:
                self.step(number - 1, a, c)
                self.step(number - 1, c, b)

    def histogram(self) -> Dict[str, int]:
        return self._histogram

    def __str__(self):
        return self._template


if __name__ == '__main__':
    from days import util

    lines = util.readinputfile('inputfiles/day14_example.txt')
    # lines = util.readinputfile('inputfiles/day14_input.txt')
    polymer = Polymer(lines)
    number = 23
    polymer.steps(number)
    histogram = polymer.histogram()
    print(histogram)
    values = list(histogram.values())
    values.sort()
    diff = values[-1] - values[0]

    util.printresultline(f'14b ({number} steps!)', diff)
