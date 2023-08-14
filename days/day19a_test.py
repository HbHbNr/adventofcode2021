"""Unit tests for https://adventofcode.com/2021/day/19 part a"""
import unittest
from days import day19a
from util import util


Position = day19a.Position
Distance = day19a.Distance
Scanner = day19a.Scanner
ScannerData = day19a.ScannerData


class TestDay19a(unittest.TestCase):

    def testVectorRotateAxes(self) -> None:
        position = Position(1, 2, 3)
        assert str(position) == 'C(1/2/3)'
        position.rotateAxes()
        assert str(position) == 'C(3/1/2)'
        position.rotateAxes()
        assert str(position) == 'C(2/3/1)'
        position.rotateAxes()
        assert str(position) == 'C(1/2/3)'

    def testVectorTurnAroundX90(self) -> None:
        position = Position(1, 2, 3)
        assert str(position) == 'C(1/2/3)'
        position.turnAroundX90()
        assert str(position) == 'C(1/-3/2)'
        position.turnAroundX90()
        assert str(position) == 'C(1/-2/-3)'
        position.turnAroundX90()
        assert str(position) == 'C(1/3/-2)'
        position.turnAroundX90()
        assert str(position) == 'C(1/2/3)'

    def testVectorTurnAroundY90(self) -> None:
        position = Position(1, 2, 3)
        assert str(position) == 'C(1/2/3)'
        position.turnAroundY90()
        assert str(position) == 'C(3/2/-1)'
        position.turnAroundY90()
        assert str(position) == 'C(-1/2/-3)'
        position.turnAroundY90()
        assert str(position) == 'C(-3/2/1)'
        position.turnAroundY90()
        assert str(position) == 'C(1/2/3)'

    def testVectorTurnAroundZ90(self) -> None:
        position = Position(1, 2, 3)
        assert str(position) == 'C(1/2/3)'
        position.turnAroundZ90()
        assert str(position) == 'C(-2/1/3)'
        position.turnAroundZ90()
        assert str(position) == 'C(-1/-2/3)'
        position.turnAroundZ90()
        assert str(position) == 'C(2/-1/3)'
        position.turnAroundZ90()
        assert str(position) == 'C(1/2/3)'

    def testVectorTurnAroundX180(self) -> None:
        position = Position(1, 2, 3)
        assert str(position) == 'C(1/2/3)'
        position.turnAroundX180()
        assert str(position) == 'C(1/-2/-3)'
        position.turnAroundX180()
        assert str(position) == 'C(1/2/3)'

    def testVectorTurnAroundY180(self) -> None:
        position = Position(1, 2, 3)
        assert str(position) == 'C(1/2/3)'
        position.turnAroundY180()
        assert str(position) == 'C(-1/2/-3)'
        position.turnAroundY180()
        assert str(position) == 'C(1/2/3)'

    def testVectorTurnAroundZ180(self) -> None:
        position = Position(1, 2, 3)
        assert str(position) == 'C(1/2/3)'
        position.turnAroundZ180()
        assert str(position) == 'C(-1/-2/3)'
        position.turnAroundZ180()
        assert str(position) == 'C(1/2/3)'

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
