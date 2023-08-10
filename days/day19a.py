"""Solution for https://adventofcode.com/2021/day/19 part a"""
from typing import List, NamedTuple, Tuple
from util import util


class Coords(NamedTuple):

    x: int
    y: int
    z: int


class Distance(NamedTuple):

    dx: int
    dy: int
    dz: int


class Scanner:
    # pylint: disable=too-few-public-methods

    def __init__(self, name) -> None:
        self._name: str = name
        self._beaconPositions: List[Coords] = []
        print(self._name)

    def addBeaconPosition(self, beaconPosition):
        self._beaconPositions.append(beaconPosition)


class ScannerData:
    # pylint: disable=too-few-public-methods

    def __init__(self, lines: Tuple[str, ...]) -> None:
        self._scanners: List[Scanner] = []
        scanner: Scanner
        beaconCount: int = 0
        for line in lines:
            if line == '':
                continue
            if line[1] == '-':
                scanner = Scanner(line[4:-4])
                # print(f'New scanner: {scanner}')
                self._scanners.append(scanner)
            else:
                x, y, z = line.split(',')
                beaconPosition = Coords(int(x), int(y), int(z))
                scanner.addBeaconPosition(beaconPosition)
                beaconCount += 1
        print(f'Found {len(self._scanners)} scanners and {beaconCount} beacons')

    def getScanners(self) -> List[Scanner]:
        return self._scanners


def main():
    lines = util.readinputfile('inputfiles/day19_example.txt')
    # lines = util.readinputfile('inputfiles/day19_input.txt')
    _ = ScannerData(lines)

    util.printresultline('19a', '???')


if __name__ == '__main__':
    main()
