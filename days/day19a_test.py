"""Unit tests for https://adventofcode.com/2021/day/19 part a"""
import unittest
from days import day19a
from util import util


Scanner = day19a.Scanner
ScannerData = day19a.ScannerData


class TestDay19a(unittest.TestCase):

    def testExample(self) -> None:
        lines = util.readinputfile('inputfiles/day19_example.txt')
        scannerData: ScannerData = day19a.ScannerData(lines)

        assert len(scannerData.getScanners()) == 5

    def testInput(self) -> None:
        lines = util.readinputfile('inputfiles/day19_input.txt')
        scannerData: ScannerData = day19a.ScannerData(lines)

        assert len(scannerData.getScanners()) == 28
