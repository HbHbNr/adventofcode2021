"""Solution for https://adventofcode.com/2021/day/19 part a"""
from typing import List, Tuple, Dict
import itertools
from util import util


ScannerBeaconPair = Tuple['Scanner', 'Beacon', 'Beacon']
DistanceMap = Dict['Distance', List[ScannerBeaconPair]]
OverlappingBeaconMap = Dict['Beacon', List['Beacon']]
OverlappingScannerMap = Dict[Tuple['Scanner', 'Scanner'], OverlappingBeaconMap]


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


class Position(Vector):
    # pylint: disable=too-few-public-methods

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'C({self.x}/{self.y}/{self.z})'


class Distance(Vector):
    # pylint: disable=too-few-public-methods

    @classmethod
    def betweenPositions(cls, position1: Position, position2: Position) -> 'Distance':
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

    def __init__(self, name: str, scanner: 'Scanner', position: Position):
        self._name = name
        self._scanner: 'Scanner' = scanner
        self._position: Position = position

    def getPosition(self) -> Position:
        return self._position

    def __lt__(self, other: 'Beacon') -> bool:
        return self._name < other._name

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Beacon{self._name}({self._scanner};{self._position.x}/{self._position.y}/{self._position.z})'


class Scanner:
    # pylint: disable=too-few-public-methods

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._beacons: List[Beacon] = []
        self._distances: List[Distance] = []
        # print(self._name)

    def addBeacon(self, beacon: Beacon) -> None:
        self._beacons.append(beacon)

    def calcDistances(self, distanceMap: DistanceMap) -> int:
        distanceCount = 0
        for beacon1, beacon2 in itertools.combinations(self._beacons, 2):
            distance: Distance = Distance.betweenPositions(beacon1.getPosition(), beacon2.getPosition())
            # distance.turnLongestToPositiveX()
            distance.unify()
            self._distances.append(distance)
            scannerBeaconPair: ScannerBeaconPair = (self, beacon1, beacon2)
            if distance not in distanceMap:
                distanceMap[distance] = [scannerBeaconPair]
            else:
                distanceMap[distance].append(scannerBeaconPair)
            distanceCount += 1
        return distanceCount

    def __lt__(self, other: 'Scanner') -> bool:
        return self._name < other._name

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Scanner{self._name}'


class ScannerData:
    # pylint: disable=too-few-public-methods

    def __init__(self, lines: Tuple[str, ...]) -> None:
        self._scanners: List[Scanner] = []
        self._beacons: List[Beacon] = []
        scanner: Scanner
        for line in lines:
            if line == '':
                continue
            if line[1] == '-':
                scanner = Scanner(line[12:-4])
                # print(f'New scanner: {scanner}')
                self._scanners.append(scanner)
            else:
                x, y, z = line.split(',')
                beacon = Beacon(str(len(self._beacons)), scanner, Position(int(x), int(y), int(z)))
                self._beacons.append(beacon)
                scanner.addBeacon(beacon)
        print(f'Found {len(self._scanners)} scanners and {len(self._beacons)} beacons')

        self._distanceMap: DistanceMap = {}
        for scanner in self._scanners:
            _ = scanner.calcDistances(self._distanceMap)
            # print(distances)

        self._overlappingScannerMap: OverlappingScannerMap = {}
        for _, scannerBeaconPairs in self._distanceMap.items():
            if len(scannerBeaconPairs) > 1:
                for scannerBeaconPair0, scannerBeaconPair1 in itertools.combinations(scannerBeaconPairs, 2):
                    ScannerData.addToOverlappingScannerMap(self._overlappingScannerMap, scannerBeaconPair0, scannerBeaconPair1)
        for scannerPair, overlappingBeaconMap in self._overlappingScannerMap.items():
            print(scannerPair)
            for beacon, beaconList in overlappingBeaconMap.items():
                print(f'{beacon}: {beaconList}')
            print()

        self._realBeacons = self.filterOverlappingBeacons()
        print(self._realBeacons)

    @classmethod
    def addToOverlappingScannerMap(cls, overlappingScannerMap: OverlappingScannerMap,
                                   scannerBeaconPair0: ScannerBeaconPair, scannerBeaconPair1: ScannerBeaconPair) -> None:
        scanner0: Scanner = scannerBeaconPair0[0]
        scanner0Beacon0: Beacon = scannerBeaconPair0[1]
        scanner0Beacon1: Beacon = scannerBeaconPair0[2]
        scanner1: Scanner = scannerBeaconPair1[0]
        scanner1Beacon0: Beacon = scannerBeaconPair1[1]
        scanner1Beacon1: Beacon = scannerBeaconPair1[2]
        scannerPair = (scanner0, scanner1)
        if scannerPair not in overlappingScannerMap:
            overlappingScannerMap[scannerPair] = {}
        for scanner0Beacon in [scanner0Beacon0, scanner0Beacon1]:
            if scanner0Beacon not in overlappingScannerMap[scannerPair]:
                overlappingScannerMap[scannerPair][scanner0Beacon] = [scanner1Beacon0, scanner1Beacon1]
            else:
                beaconList = overlappingScannerMap[scannerPair][scanner0Beacon]
                if len(beaconList) == 1:
                    if beaconList[0] == scanner1Beacon0 or beaconList[0] == scanner1Beacon1:
                        continue  # only one entry, and that one is right
                    raise ValueError(f'{scanner0Beacon} mapped to {beaconList[0]}, '
                                     'but now found {scanner1Beacon0} and {scanner1Beacon1}')
                # so beaconList has 2 entries, but only might be correct:
                if len(beaconList) == 2:
                    # TO------DO: make 4 checks and remove the wrong entry
                    if scanner1Beacon0 in beaconList:
                        beaconList.clear()
                        beaconList.append(scanner1Beacon0)
                    elif scanner1Beacon1 in beaconList:
                        beaconList.clear()
                        beaconList.append(scanner1Beacon1)
                    else:
                        raise ValueError(f'{scanner0Beacon} mapped to BeaconList {beaconList}, '
                                         'but now found {scanner1Beacon0} and {scanner1Beacon1}')
                else:
                    raise ValueError(f'BeaconList {beaconList} has too many entries: {len(beaconList)}')

    def filterOverlappingBeacons(self) -> List[Beacon]:
        realBeacons = self._beacons.copy()
        # Dict['Beacon', List['Beacon']]
        for overlappingBeaconMap in self._overlappingScannerMap.values():
            for beacon, beaconList in overlappingBeaconMap.items():
                if beacon in realBeacons:
                    overlappingBeacon = beaconList[0]
                    if overlappingBeacon in realBeacons:
                        realBeacons.remove(overlappingBeacon)
        return realBeacons

    def getScanners(self) -> List[Scanner]:
        return self._scanners

    def getDistanceMap(self) -> DistanceMap:
        return self._distanceMap

    def getOverlappingScannerMap(self) -> OverlappingScannerMap:
        return self._overlappingScannerMap

    def getRealBeacons(self) -> List[Beacon]:
        return self._realBeacons


def main():
    # lines = util.readinputfile('inputfiles/day19_example1.txt')
    lines = util.readinputfile('inputfiles/day19_example2.txt')
    # lines = util.readinputfile('inputfiles/day19_input.txt')
    scannerData = ScannerData(lines)

    # distanceMap = scannerData.getDistanceMap()
    # for distance, markers in distanceMap.items():
    #     if len(markers) > 1:
    #         print(distance)
    #         print('   ', markers)

    # overlappingScannerMap = scannerData.getOverlappingScannerMap()
    # for scannerPair, counter in sorted(overlappingScannerMap.items()):
    #     print(f'Overlapping of {scannerPair}: {counter}')

    realBeacons = scannerData.getRealBeacons()

    util.printresultline('19a', len(realBeacons))


if __name__ == '__main__':
    main()
