class Aligner:
    def __init__(self, line):
        self._crabs = tuple([int(crab) for crab in line.split(',')])

    def __str__(self):
        return str(self._crabs)

    def size(self):
        return len(self._crabs)

    def calcbestx(self):
        bestx = None
        totalfuels = {}
        for testpos in range(min(self._crabs), max(self._crabs) + 1):
            distances = [int(abs(testpos - crab)) for crab in self._crabs]
            totalfuels[testpos] = sum(distances)
            if bestx is None or totalfuels[bestx] > totalfuels[testpos]:
                bestx = testpos

        alignment = {'bestx': bestx, 'totalfuels': totalfuels}
        return alignment


if __name__ == '__main__':
    import util

    # lines = util.readinputfile('inputfiles/day7_example.txt')
    lines = util.readinputfile('inputfiles/day7_input.txt')
    aligner = Aligner(lines[0])
    print('crabs: {}'.format(aligner.size()))
    alignment = aligner.calcbestx()
    print('bestx: {}  bestfuel: {}'.format(alignment['bestx'], alignment['totalfuels'][alignment['bestx']]))
