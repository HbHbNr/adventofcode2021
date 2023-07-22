"""Solution for https://adventofcode.com/2021/day/1 part a"""
import fileinput
from util import util


def sweep():
    inputfile = "inputfiles/day1_input.txt"
    firstline = True
    lastvalue = 0
    increments = 0
    for line in fileinput.input(inputfile):
        value = int(line)
        if firstline:
            firstline = False
        elif value > lastvalue:
            increments += 1
        lastvalue = value
    return increments


def main():
    increments = sweep()

    util.printresultline('1a', increments)


if __name__ == '__main__':
    main()
