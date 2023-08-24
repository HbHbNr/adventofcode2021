"""Solution for https://adventofcode.com/2021/day/19 part a"""
from typing import List, Tuple, Dict, Set, Optional
import itertools
from util import util, vector


ScannerPair = Tuple['Scanner', 'Scanner']
ScannerBeaconPair = Tuple['Scanner', 'Beacon', 'Beacon']
DistanceMap = Dict['Distance', List[ScannerBeaconPair]]
OverlappingBeaconMap = Dict['Beacon', List['Beacon']]
OverlappingScannerMap = Dict[ScannerPair, OverlappingBeaconMap]


class Position(vector.Vector):
    # pylint: disable=too-few-public-methods

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'C({self.x}/{self.y}/{self.z})'


class Distance(vector.Vector):
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

    def unify(self) -> 'Distance':
        coords: List[int] = [abs(self.x), abs(self.y), abs(self.z)]
        coords.sort(reverse=True)
        return Distance(*coords)

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
            distance = distance.unify()
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

        # read scanner and beacon data
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

        # calculate a map of distances
        self._distanceMap: DistanceMap = {}
        for scanner in self._scanners:
            _ = scanner.calcDistances(self._distanceMap)
            # print(distances)

        self._overlappingScannerMap: OverlappingScannerMap = {}
        for _, scannerBeaconPairs in self._distanceMap.items():
            if len(scannerBeaconPairs) > 1:
                for scannerBeaconPair0, scannerBeaconPair1 in itertools.combinations(scannerBeaconPairs, 2):
                    ScannerData.addToOverlappingScannerMap(self._overlappingScannerMap, scannerBeaconPair0, scannerBeaconPair1)

        self.cleanOverlappingScannerMap()
        self._scannerDependencyPath = self.findScannerDependencyPath()
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
                beaconList: List[Beacon] = overlappingScannerMap[scannerPair][scanner0Beacon]
                if len(beaconList) == 1:
                    if beaconList[0] == scanner1Beacon0 or beaconList[0] == scanner1Beacon1:
                        continue  # only one entry, and that one is right
                    raise ValueError(f'{scanner0Beacon} mapped to {beaconList[0]}, '
                                     'but now found {scanner1Beacon0} and {scanner1Beacon1}')
                # so beaconList has 2 entries, but only might be correct:
                if len(beaconList) == 2:
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

    def cleanOverlappingScannerMap(self) -> None:
        scannerPairs: List[ScannerPair] = list(self._overlappingScannerMap.keys())
        for scannerPair in scannerPairs:
            overlappingBeaconMap: OverlappingBeaconMap = self._overlappingScannerMap[scannerPair]
            if len(overlappingBeaconMap) < 12:
                # the two scanners do not have at least 12 overlapping beacons
                del self._overlappingScannerMap[scannerPair]
            else:
                print(scannerPair)
                for beacon, beaconList in overlappingBeaconMap.items():
                    print(f'{beacon}: {beaconList[0]}')
                print()

    def findScannerDependencyPath(self) -> List[ScannerPair]:
        # We know which scanners have overlapping beacons, now we need to find a path from
        # scanner 0 to all the other scanners. The dictionary self._overlappingScannerMap has
        # all scanner pairs as keys, but in a random order. We need to order this list
        # depending on the overlapping beacons.
        scannerDependencyPath: List[ScannerPair] = []
        fixedScanners: Set[Scanner] = {self._scanners[0]}  # at start, only scanner 0 is fixed
        floatingScannerPairs: List[ScannerPair] = list(self._overlappingScannerMap.keys())
        while len(fixedScanners) < len(self._scanners):
            for i in range(len(floatingScannerPairs)):  # pylint: disable=consider-using-enumerate
                floatingScannerPair = floatingScannerPairs[i]
                fixedScannerPair: ScannerPair = floatingScannerPair
                newFixedScanner: Optional[Scanner] = None
                if floatingScannerPair[0] in fixedScanners:
                    # left side of the pair is already fixed
                    newFixedScanner = floatingScannerPair[1]
                elif floatingScannerPair[1] in fixedScanners:
                    # right side of the pair is already fixed
                    newFixedScanner = floatingScannerPair[0]
                    fixedScannerPair = (floatingScannerPair[1], floatingScannerPair[0])  # swap
                if newFixedScanner is not None:
                    print(fixedScannerPair)
                    print(newFixedScanner)
                    fixedScanners.add(newFixedScanner)
                    scannerDependencyPath.append(fixedScannerPair)
                    del floatingScannerPairs[i]
                    break
        return scannerDependencyPath

    def filterOverlappingBeacons(self) -> List[Beacon]:
        realBeacons = self._beacons.copy()
        # Dict['Beacon', List['Beacon']]
        for scannerPair in self._scannerDependencyPath:
            if scannerPair in self._overlappingScannerMap:
                overlappingBeaconMap = self._overlappingScannerMap[scannerPair]
                for beaconList in overlappingBeaconMap.values():
                    overlappingBeacon = beaconList[0]
                    if overlappingBeacon in realBeacons:
                        realBeacons.remove(overlappingBeacon)
            else:
                # the dependency is the opposite direction
                scannerPair = (scannerPair[1], scannerPair[0])
                overlappingBeaconMap = self._overlappingScannerMap[scannerPair]
                for overlappingBeacon in overlappingBeaconMap.keys():
                    if overlappingBeacon in realBeacons:
                        realBeacons.remove(overlappingBeacon)
        return realBeacons

    def getScanners(self) -> List[Scanner]:
        return self._scanners

    def getDistanceMap(self) -> DistanceMap:
        return self._distanceMap

    def getOverlappingScannerMap(self) -> OverlappingScannerMap:
        return self._overlappingScannerMap

    def getScannerDependencyPath(self) -> List[ScannerPair]:
        return self._scannerDependencyPath

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

    scannerDependencyPath = scannerData.getScannerDependencyPath()
    print(scannerDependencyPath)
    realBeacons = scannerData.getRealBeacons()

    util.printresultline('19a', len(realBeacons))


if __name__ == '__main__':
    main()
