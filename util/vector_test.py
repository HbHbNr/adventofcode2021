"""Unit tests for the Vector class"""
import unittest
import util

Vector = util.vector.Vector


class TestVector(unittest.TestCase):

    def testCopy(self) -> None:
        vector1 = Vector(1, 2, 3)
        vector2 = vector1.copy()
        assert vector1 == vector2

    def testRotateAxes(self) -> None:
        vector1 = Vector(1, 2, 3)
        assert str(vector1) == 'V(1/2/3)'
        vector = vector1.rotateAxes()
        assert str(vector) == 'V(3/1/2)'
        vector = vector.rotateAxes()
        assert str(vector) == 'V(2/3/1)'
        vector = vector.rotateAxes()
        assert vector1 == vector

    def testTurnAroundX90(self) -> None:
        vector1 = Vector(1, 2, 3)
        assert str(vector1) == 'V(1/2/3)'
        vector = vector1.turnAroundX90()
        assert str(vector) == 'V(1/-3/2)'
        vector = vector.turnAroundX90()
        assert str(vector) == 'V(1/-2/-3)'
        vector = vector.turnAroundX90()
        assert str(vector) == 'V(1/3/-2)'
        vector = vector.turnAroundX90()
        assert vector1 == vector

    def testTurnAroundY90(self) -> None:
        vector1 = Vector(1, 2, 3)
        assert str(vector1) == 'V(1/2/3)'
        vector = vector1.turnAroundY90()
        assert str(vector) == 'V(3/2/-1)'
        vector = vector.turnAroundY90()
        assert str(vector) == 'V(-1/2/-3)'
        vector = vector.turnAroundY90()
        assert str(vector) == 'V(-3/2/1)'
        vector = vector.turnAroundY90()
        assert vector1 == vector

    def testTurnAroundZ90(self) -> None:
        vector1 = Vector(1, 2, 3)
        assert str(vector1) == 'V(1/2/3)'
        vector = vector1.turnAroundZ90()
        assert str(vector) == 'V(-2/1/3)'
        vector = vector.turnAroundZ90()
        assert str(vector) == 'V(-1/-2/3)'
        vector = vector.turnAroundZ90()
        assert str(vector) == 'V(2/-1/3)'
        vector = vector.turnAroundZ90()
        assert vector1 == vector

    def testTurnAroundX180(self) -> None:
        vector1 = Vector(1, 2, 3)
        assert str(vector1) == 'V(1/2/3)'
        vector = vector1.turnAroundX180()
        assert str(vector) == 'V(1/-2/-3)'
        vector = vector.turnAroundX180()
        assert vector1 == vector

    def testTurnAroundY180(self) -> None:
        vector1 = Vector(1, 2, 3)
        assert str(vector1) == 'V(1/2/3)'
        vector = vector1.turnAroundY180()
        assert str(vector) == 'V(-1/2/-3)'
        vector = vector.turnAroundY180()
        assert vector1 == vector

    def testTurnAroundZ180(self) -> None:
        vector1 = Vector(1, 2, 3)
        assert str(vector1) == 'V(1/2/3)'
        vector = vector1.turnAroundZ180()
        assert str(vector) == 'V(-1/-2/3)'
        vector = vector.turnAroundZ180()
        assert vector1 == vector

    def testReverse(self) -> None:
        vector1 = Vector(1, 2, 3)
        vector = vector1.reverse()
        assert vector1.x == -vector.x
        assert vector1.y == -vector.y
        assert vector1.z == -vector.z
        vector = vector.reverse()
        assert vector1 == vector

    def testHash(self) -> None:
        vector = Vector(1, 2, 3)
        assert hash(vector) != 0

    def testRepr(self) -> None:
        vector = Vector(1, 2, 3)
        assert repr(vector) == str(vector)
