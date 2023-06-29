import fileinput


def readinputfile(inputfile):
    lines = []
    for line in fileinput.input(inputfile):
        lines.append(line.rstrip())
    return tuple(lines)


def readhexinputfile(inputfile) -> bytes:
    line: str = fileinput.input(inputfile).readline().rstrip()
    print(line)
    return bytes.fromhex(line)


def printresultline(day, result):
    print('Day {:>3}: {}'.format(day, result))
