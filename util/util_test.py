"""Unit tests for the collection of utility functions"""
import unittest
from util import util


class TestByteStream(unittest.TestCase):

    def testReadInputfile(self):
        lines = util.readinputfile('inputfiles/day01_example.txt')
        print(lines)
        self.assertEqual(lines, tuple(['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']))

    def testReadHexInputfile(self):
        _bytes = util.readhexinputfile('inputfiles/day16_example.txt')
        self.assertEqual(_bytes, bytes([0x8A, 0x00, 0x4A, 0x80, 0x1A, 0x80, 0x02, 0xF4, 0x78]))

    def testPrintResultline(self):
        util.printresultline('99a', -1)
