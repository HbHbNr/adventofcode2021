"""Unit tests for the Vector class"""
import unittest
import util

Vector = util.vector.Vector


class TestVector(unittest.TestCase):

    def testVectorRotateAxes(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.rotateAxes()
        assert str(vector) == 'V(3/1/2)'
        vector.rotateAxes()
        assert str(vector) == 'V(2/3/1)'
        vector.rotateAxes()
        assert str(vector) == 'V(1/2/3)'

    def testVectorTurnAroundX90(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.turnAroundX90()
        assert str(vector) == 'V(1/-3/2)'
        vector.turnAroundX90()
        assert str(vector) == 'V(1/-2/-3)'
        vector.turnAroundX90()
        assert str(vector) == 'V(1/3/-2)'
        vector.turnAroundX90()
        assert str(vector) == 'V(1/2/3)'

    def testVectorTurnAroundY90(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.turnAroundY90()
        assert str(vector) == 'V(3/2/-1)'
        vector.turnAroundY90()
        assert str(vector) == 'V(-1/2/-3)'
        vector.turnAroundY90()
        assert str(vector) == 'V(-3/2/1)'
        vector.turnAroundY90()
        assert str(vector) == 'V(1/2/3)'

    def testVectorTurnAroundZ90(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.turnAroundZ90()
        assert str(vector) == 'V(-2/1/3)'
        vector.turnAroundZ90()
        assert str(vector) == 'V(-1/-2/3)'
        vector.turnAroundZ90()
        assert str(vector) == 'V(2/-1/3)'
        vector.turnAroundZ90()
        assert str(vector) == 'V(1/2/3)'

    def testVectorTurnAroundX180(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.turnAroundX180()
        assert str(vector) == 'V(1/-2/-3)'
        vector.turnAroundX180()
        assert str(vector) == 'V(1/2/3)'

    def testVectorTurnAroundY180(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.turnAroundY180()
        assert str(vector) == 'V(-1/2/-3)'
        vector.turnAroundY180()
        assert str(vector) == 'V(1/2/3)'

    def testVectorTurnAroundZ180(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.turnAroundZ180()
        assert str(vector) == 'V(-1/-2/3)'
        vector.turnAroundZ180()
        assert str(vector) == 'V(1/2/3)'
