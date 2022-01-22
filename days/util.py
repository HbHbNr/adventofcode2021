import fileinput


def readinputfile(inputfile):
    lines = []
    for line in fileinput.input(inputfile):
        lines.append(line.rstrip())
    return tuple(lines)
