"""Unit tests for the Vector class"""
import unittest
import util

Vector = util.vector.Vector


class TestVector(unittest.TestCase):

    def testClone(self) -> None:
        vector1 = Vector(1, 2, 3)
        vector2 = vector1.clone()
        assert vector1 == vector2

    def testRotateAxes(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.rotateAxes()
        assert str(vector) == 'V(3/1/2)'
        vector.rotateAxes()
        assert str(vector) == 'V(2/3/1)'
        vector.rotateAxes()
        assert str(vector) == 'V(1/2/3)'

    def testTurnAroundX90(self) -> None:
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

    def testTurnAroundY90(self) -> None:
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

    def testTurnAroundZ90(self) -> None:
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

    def testTurnAroundX180(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.turnAroundX180()
        assert str(vector) == 'V(1/-2/-3)'
        vector.turnAroundX180()
        assert str(vector) == 'V(1/2/3)'

    def testTurnAroundY180(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.turnAroundY180()
        assert str(vector) == 'V(-1/2/-3)'
        vector.turnAroundY180()
        assert str(vector) == 'V(1/2/3)'

    def testTurnAroundZ180(self) -> None:
        vector = Vector(1, 2, 3)
        assert str(vector) == 'V(1/2/3)'
        vector.turnAroundZ180()
        assert str(vector) == 'V(-1/-2/3)'
        vector.turnAroundZ180()
        assert str(vector) == 'V(1/2/3)'

    def testReverse(self) -> None:
        vector1 = Vector(1, 2, 3)
        vector2 = vector1.clone().reverse()
        assert vector1.x == -vector2.x
        assert vector1.y == -vector2.y
        assert vector1.z == -vector2.z

    def testHash(self) -> None:
        vector = Vector(1, 2, 3)
        assert hash(vector) != 0

    def testRepr(self) -> None:
        vector = Vector(1, 2, 3)
        assert repr(vector) == str(vector)
