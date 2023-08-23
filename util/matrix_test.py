"""Unit tests for the Matrix class"""
import unittest
import util

Matrix3x3 = util.matrix.Matrix3x3


class TestMatrix(unittest.TestCase):

    def testInit(self) -> None:
        identity = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        matrix = Matrix3x3(*identity)
        assert str(matrix) == 'M(1/0/0 0/1/0 0/0/1)'
