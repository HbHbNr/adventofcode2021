import fileinput


def readinputfile(inputfile):
    lines = []
    for line in fileinput.input(inputfile):
        lines.append(line.rstrip())
    return tuple(lines)


def printresultline(day, result):
    print('Day {:>3}: {}'.format(day, result))
