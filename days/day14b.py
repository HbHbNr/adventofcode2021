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
        template: List[Tuple[str, int]] = [(element, number) for element in self._template]
        length = len(template)
        while length > 0:
            if length > 1:  # examine first two elements
                a = template[0]
                b = template[1]
                a1 = a[1]
                b1 = b[1]
                # (at least) one element is at the lowest level
                if a1 == 0 or b1 == 0:
                    # print(a[0], b[0], sep='', end='')
                    template = template[2:]  # remove first two elements
                    length -= 2
                # no element is at the lowest level
                else:
                    key = (a[0], b[0])
                    c: str = self._rules[key]
                    self._histogram[c] += 1
                    if a1 < b1:
                        template.insert(1, (c, a1 - 1))
                    else:
                        template.insert(1, (c, b1 - 1))
                    length += 1
            elif length == 1:  # last element of template
                # print(template[0][0])
                break
        # print()

    def histogram(self) -> Dict[str, int]:
        return self._histogram

    def __str__(self):
        return self._template


if __name__ == '__main__':
    from days import util
    import sys

    lines = util.readinputfile('inputfiles/day14_example.txt')
    # lines = util.readinputfile('inputfiles/day14_input.txt')
    polymer = Polymer(lines)
    number = 21
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
