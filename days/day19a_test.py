"""Unit tests for https://adventofcode.com/2021/day/19 part a"""
import unittest
from days import day19a
from util import util


Position = day19a.Position
Distance = day19a.Distance
Scanner = day19a.Scanner
ScannerData = day19a.ScannerData


class TestDay19a(unittest.TestCase):

    # def testDistanceTurnLongestToPositiveX(self):
    #     distance = Distance(1, 2, -3)
    #     assert str(distance) == 'D(1/2/-3)'
    #     distance.turnLongestToPositiveX()
    #     assert str(distance) == 'D(3/-1/-2)'

    def testDistanceUnify(self):
        distance = Distance(1, 2, -3)
        assert str(distance) == 'D(1/2/-3)'
        distance.unify()
        assert str(distance) == 'D(3/2/1)'

    def testExample(self) -> None:
        lines = util.readinputfile('inputfiles/day19_example2.txt')
        scannerData: ScannerData = day19a.ScannerData(lines)

        assert len(scannerData.getScanners()) == 5

    def testInput(self) -> None:
        lines = util.readinputfile('inputfiles/day19_input.txt')
        scannerData: ScannerData = day19a.ScannerData(lines)

        assert len(scannerData.getScanners()) == 28
