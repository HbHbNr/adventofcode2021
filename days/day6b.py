from util import util


class School:
    def __init__(self, line):
        self._fishstats = [0 for x in range(9)]
        for fish in line.split(','):
            self._fishstats[int(fish)] += 1

    def __str__(self):
        return str(self._fishstats)

    def size(self):
        return sum(self._fishstats)

    def nextday(self):
        creators = self._fishstats[0]
        for index in range(len(self._fishstats) - 1):
            self._fishstats[index] = self._fishstats[index + 1]
        self._fishstats[6] += creators
        self._fishstats[8] = creators

    def nextdays(self, days, progress=False):
        for day in range(1, days + 1):
            if progress:
                print(f'Day {day}')
            self.nextday()


def main():
    # lines = util.readinputfile('inputfiles/day6_example.txt')
    lines = util.readinputfile('inputfiles/day6_input.txt')
    school = School(lines[0])
    print(school.size())
    # print(school)
    school.nextdays(256, False)
    print(school.size())
    # print(school)


if __name__ == '__main__':
    main()
