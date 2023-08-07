"""Collection of utility functions"""
import fileinput
from typing import Tuple


def readinputfile(inputfile: str) -> Tuple[str, ...]:
    """ Read all lines from inputfile and store them in a tuple of strings, with removed newlines. """
    lines = []
    for line in fileinput.input(inputfile):
        lines.append(line.rstrip())
    return tuple(lines)


def readhexinputfile(inputfile: str) -> bytes:
    """ Read all lines from inputfile and create 'bytes' object from the data. """
    lines = readinputfile(inputfile)
    line = ''.join(lines)
    return bytes.fromhex(line)


def printresultline(day, result):
    print(f'Day {day:>3}: {result}')
