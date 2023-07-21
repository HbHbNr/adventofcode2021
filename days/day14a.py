from typing import List, Tuple, Dict
from util import util


class Polymer:

    def __init__(self, lines: List[str]) -> None:
        self._template = lines[0]
        self._rules: Dict[Tuple[str, str], str] = {}

        for line in lines[2:]:
            key = line[0], line[1]
            value = line[6]
            self._rules[key] = value
        # print(self._rules)

    def step(self) -> None:
        newtemplate: List[str] = []
        for i in range(0, len(self._template) - 1):
            left = self._template[i]
            right = self._template[i + 1]
            key = (left, right)
            middle = self._rules.get(key)
            newtemplate.append(left)
            if middle is not None:
                newtemplate.append(middle)
        newtemplate.append(self._template[-1])
        self._template = ''.join(newtemplate)
        # print(self._template)

    def histogram(self) -> Dict[str, int]:
        histogram: Dict[str, int] = {}
        for char in self._template:
            if char in histogram:
                histogram[char] += 1
            else:
                histogram[char] = 1
        return histogram

    def __str__(self):
        return self._template


def main():
    # lines = util.readinputfile('inputfiles/day14_example.txt')
    lines = util.readinputfile('inputfiles/day14_input.txt')
    polymer = Polymer(lines)
    for _ in range(1, 10 + 1):
        polymer.step()
        # print(f'{step} - {len(str(polymer))}')
    histogram = polymer.histogram()
    # print(histogram)
    values = list(histogram.values())
    values.sort()
    diff = values[-1] - values[0]

    util.printresultline('14a', diff)


if __name__ == '__main__':
    main()
