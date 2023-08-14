"""Solution for https://adventofcode.com/2021/day/19 part a"""
from typing import List, Tuple, Dict
import itertools
from util import util


DistanceMap = Dict['Distance', List[Tuple['Scanner', 'Beacon', 'Beacon']]]


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

    def reverse(self) -> None:
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'V({self.x}/{self.y}/{self.z})'


class Coords(Vector):
    # pylint: disable=too-few-public-methods

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'C({self.x}/{self.y}/{self.z})'


class Distance(Vector):
    # pylint: disable=too-few-public-methods

    @classmethod
    def betweenPositions(cls, position1: Coords, position2: Coords) -> 'Distance':
        distance = Distance(position2.x - position1.x, position2.y - position1.y, position2.z - position1.z)
        return distance

    # def turnLongestToPositiveX(self) -> None:
    #     old = str(self)
    #     print('  toX_strt:', old, sep='')
    #     while abs(self.x) < abs(self.y) or abs(self.x) < abs(self.z):
    #         self.rotateAxes()
    #         print('      rotA:', old, '->', self, sep='')
    #     if self.x < 0:
    #         # self.turnAroundY180()
    #         # print('  toX_Y180:', old, '->', self, sep='')
    #         self.reverse()
    #         print('      rvrs:', old, '->', self, sep='')
    #     print('  toX_stop:', old, '->', self, sep='')

    def unify(self) -> None:
        coords: List[int] = [abs(self.x), abs(self.y), abs(self.z)]
        coords.sort(reverse=True)
        self.x, self.y, self.z = coords

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'D({self.x}/{self.y}/{self.z})'


class Beacon:
    # pylint: disable=too-few-public-methods

    def __init__(self, name: str, scanner: 'Scanner', position: Coords):
        self._name = name
        self._scanner: 'Scanner' = scanner
        self._position: Coords = position

    def getPosition(self) -> Coords:
        return self._position

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Beacon({self._name}:{self._position.x}/{self._position.y}/{self._position.z})'


class Scanner:
    # pylint: disable=too-few-public-methods

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._beacons: List[Beacon] = []
        self._distances: List[Distance] = []
        print(self._name)

    def addBeacon(self, beacon: Beacon) -> None:
        self._beacons.append(beacon)

    def calcDistances(self, distanceMap: DistanceMap) -> int:
        distanceCount = 0
        for beacon1, beacon2 in itertools.combinations(self._beacons, 2):
            distance: Distance = Distance.betweenPositions(beacon1.getPosition(), beacon2.getPosition())
            # distance.turnLongestToPositiveX()
            distance.unify()
            self._distances.append(distance)
            marker: Tuple['Scanner', Beacon, Beacon] = (self, beacon1, beacon2)
            if distance not in distanceMap:
                distanceMap[distance] = [marker]
            else:
                distanceMap[distance].append(marker)
            distanceCount += 1
        return distanceCount

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Scanner({self._name})'


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
                scanner = Scanner(line[12:-4])
                # print(f'New scanner: {scanner}')
                self._scanners.append(scanner)
            else:
                x, y, z = line.split(',')
                beacon = Beacon(str(beaconCount), scanner, Coords(int(x), int(y), int(z)))
                scanner.addBeacon(beacon)
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
    # lines = util.readinputfile('inputfiles/day19_example1.txt')
    lines = util.readinputfile('inputfiles/day19_example2.txt')
    # lines = util.readinputfile('inputfiles/day19_input.txt')
    scannerData = ScannerData(lines)
    distanceMap = scannerData.getDistanceMap()
    for distance, markers in distanceMap.items():
        if len(markers) > 1:
            print(distance)
            print('   ', markers)

    util.printresultline('19a', '???')


if __name__ == '__main__':
    main()
