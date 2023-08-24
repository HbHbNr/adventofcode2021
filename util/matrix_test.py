"""Unit tests for the Matrix class"""
import unittest
from util import matrix

Matrix3x3 = matrix.Matrix3x3


class TestMatrix(unittest.TestCase):

    def testInit(self) -> None:
        identity = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        matrix3x3 = Matrix3x3(*identity)
        assert str(matrix3x3) == 'M(1/0/0 0/1/0 0/0/1)'
