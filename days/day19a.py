"""Solution for https://adventofcode.com/2021/day/19 part a"""
from typing import List, Tuple, Dict
import itertools
from util import util


DistanceMap = Dict['Distance', List[Tuple['Scanner', 'Coords', 'Coords']]]


class Vector:

    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def rotateAxes(self) -> None:
        tmp = self.z
        self.z = self.y
        self.y = self.x
        self.x = tmp

    def turnAroundX90(self) -> None:
        tmp = self.y
        self.y = -self.z
        self.z = tmp

    def turnAroundY90(self) -> None:
        tmp = self.x
        self.x = self.z
        self.z = -tmp

    def turnAroundZ90(self) -> None:
        tmp = self.x
        self.x = -self.y
        self.y = tmp

    def turnAroundX180(self) -> None:
        self.y = -self.y
        self.z = -self.z

    def turnAroundY180(self) -> None:
        self.x = -self.x
        self.z = -self.z

    def turnAroundZ180(self) -> None:
        self.x = -self.x
        self.y = -self.y

    def __str__(self):
        return f'({self.x}/{self.y}/{self.z})'


class Coords(Vector):
    # pylint: disable=too-few-public-methods

    pass


class Distance(Vector):
    # pylint: disable=too-few-public-methods

    def turnLongestToPositiveX(self) -> None:
        while abs(self.x) < abs(self.y) or abs(self.x) < abs(self.z):
            self.rotateAxes()
        if self.x < 0:
            self.turnAroundY180()


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
            distance.turnLongestToPositiveX()
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
