import fileinput
from util import util


def sweep(windowsize):
    inputfile = "inputfiles/day1_input.txt"
    lastwindow = []
    increments = 0
    for line in fileinput.input(inputfile):
        value = int(line)
        if len(lastwindow) < windowsize:
            lastwindow.append(value)
        else:
            currentwindow = lastwindow[1:]
            currentwindow.append(value)
            if sum(currentwindow) > sum(lastwindow):
                increments += 1
            lastwindow = currentwindow
        # print(lastwindow)
    return increments


def main():
    increments = sweep(3)

    util.printresultline('1b', increments)


if __name__ == '__main__':
    main()
