from typing import List, Tuple, Dict


class Polymer:

    def __init__(self, lines: List[str]) -> None:
        self._template = lines[0]
        self._rules: Dict[Tuple[str, str], str] = dict()

        for line in lines[2:]:
            key = line[0], line[1]
            value = line[6]
            self._rules[key] = value
        # print(self._rules)

    def step(self) -> None:
        newtemplate: List[str] = []
        for i in range(0, len(self._template) - 1):
            a = self._template[i]
            b = self._template[i + 1]
            key = (a, b)
            c = self._rules.get(key)
            newtemplate.append(a)
            if c is not None:
                newtemplate.append(c)
        newtemplate.append(self._template[-1])
        self._template = ''.join(newtemplate)
        # print(self._template)

    def histogram(self) -> Dict[str, int]:
        histogram: Dict[str, int] = dict()
        for c in self._template:
            if c in histogram:
                histogram[c] += 1
            else:
                histogram[c] = 1
        return histogram

    def __str__(self):
        return self._template


def main():
    from util import util

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
