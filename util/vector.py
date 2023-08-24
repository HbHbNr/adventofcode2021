"""A class for vectors"""
from typing import NamedTuple


class Vector(NamedTuple):

    x: int
    y: int
    z: int

    def copy(self) -> 'Vector':
        return Vector(self.x, self.y, self.z)

    def rotateAxes(self) -> 'Vector':
        return Vector(self.z, self.x, self.y)

    def turnAroundX90(self) -> 'Vector':
        return Vector(self.x, -self.z, self.y)

    def turnAroundY90(self) -> 'Vector':
        return Vector(self.z, self.y, -self.x)

    def turnAroundZ90(self) -> 'Vector':
        return Vector(-self.y, self.x, self.z)

    def turnAroundX180(self) -> 'Vector':
        return Vector(self.x, -self.y, -self.z)

    def turnAroundY180(self) -> 'Vector':
        return Vector(-self.x, self.y, -self.z)

    def turnAroundZ180(self) -> 'Vector':
        return Vector(-self.x, -self.y, self.z)

    def reverse(self) -> 'Vector':
        return Vector(-self.x, -self.y, -self.z)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'V({self.x}/{self.y}/{self.z})'
