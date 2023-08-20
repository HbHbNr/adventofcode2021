"""Unit tests for https://adventofcode.com/2021/day/19 part a"""
import unittest
from days import day19a
from util import util


Position = day19a.Position
Distance = day19a.Distance
Scanner = day19a.Scanner
ScannerData = day19a.ScannerData


class TestDay19a(unittest.TestCase):

    def testDistanceUnify(self):
        distance = Distance(1, 2, -3)
        assert str(distance) == 'D(1/2/-3)'
        distance.unify()
        assert str(distance) == 'D(3/2/1)'

    def testExample(self) -> None:
        lines = util.readinputfile('inputfiles/day19_example2.txt')
        scannerData: ScannerData = day19a.ScannerData(lines)
        scanners = scannerData.getScanners()

        assert len(scanners) == 5

        scanner0 = scanners[0]
        scanner1 = scanners[1]
        scanner2 = scanners[2]
        scanner3 = scanners[3]
        scanner4 = scanners[4]
        scannerDependencyPath = scannerData.getScannerDependencyPath()
        assert scannerDependencyPath == [(scanner0, scanner1),
                                         (scanner1, scanner4),
                                         (scanner4, scanner2),
                                         (scanner1, scanner3)]

        assert len(scannerData.getRealBeacons()) == 79

    def testInput(self) -> None:
        lines = util.readinputfile('inputfiles/day19_input.txt')
        scannerData: ScannerData = day19a.ScannerData(lines)

        assert len(scannerData.getScanners()) == 28
        # assert len(scannerData.getRealBeacons()) == 362  # 362 is too high
