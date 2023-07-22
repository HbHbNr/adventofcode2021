"""Solution for https://adventofcode.com/2021/day/2 part a"""
import fileinput
import sys
from util import util


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def forward(self, value):
        self.x += int(value)

    def down(self, value):
        self.y += int(value)

    def up(self, value):  # pylint: disable=invalid-name
        self.y -= int(value)


def pilot():
    inputfile = "inputfiles/day02_input.txt"
    position = Position()
    for line in fileinput.input(inputfile):
        command, _, value = line.rstrip().partition(' ')
        if command == 'forward':
            position.forward(value)
        elif command == 'down':
            position.down(value)
        elif command == 'up':
            position.up(value)
        else:
            print(f'Unknown command "{line.rstrip()}" in line {fileinput.filelineno()}')
            sys.exit(1)
    return position


def main():
    position = pilot()

    util.printresultline('2a', position.x * position.y)


if __name__ == '__main__':
    main()
