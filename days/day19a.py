"""Solution for https://adventofcode.com/2021/day/19 part a"""
from typing import List, NamedTuple, Tuple, Dict
import itertools
from util import util


DistanceMap = Dict['Distance', List[Tuple['Scanner', 'Coords', 'Coords']]]


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
        self._distances: List[Distance] = []
        print(self._name)

    def addBeaconPosition(self, beaconPosition) -> None:
        self._beaconPositions.append(beaconPosition)

    def calcDistances(self, distanceMap: DistanceMap) -> int:
        distanceCount = 0
        for beacon1, beacon2 in itertools.combinations(self._beaconPositions, 2):
            distance: Distance = Distance(beacon1.x - beacon2.x, beacon1.y - beacon2.y, beacon1.z - beacon2.z)
            # WIP: normalize distances, e.g. make the longest value the X axis, and the second longstest the Y axis
            self._distances.append(distance)
            marker: Tuple['Scanner', 'Coords', 'Coords'] = (self, beacon1, beacon2)
            if distance not in distanceMap:
                distanceMap[distance] = [marker]
            else:
                distanceMap[distance].append(marker)
            distanceCount += 1
        return distanceCount

    def __repr__(self):
        return f'Scanner("{self._name}")'


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

        self._distanceMap: DistanceMap = {}
        for scanner in self._scanners:
            print(scanner.calcDistances(self._distanceMap))

    def getScanners(self) -> List[Scanner]:
        return self._scanners

    def getDistanceMap(self) -> DistanceMap:
        return self._distanceMap


def main():
    lines = util.readinputfile('inputfiles/day19_example.txt')
    # lines = util.readinputfile('inputfiles/day19_input.txt')
    scannerData = ScannerData(lines)
    distanceMap = scannerData.getDistanceMap()
    for distance, markers in distanceMap.items():
        print(distance)
        print('   ', markers)

    util.printresultline('19a', '???')


if __name__ == '__main__':
    main()
