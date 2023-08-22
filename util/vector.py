"""A class for vectors"""


class Vector:

    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def clone(self) -> 'Vector':
        return Vector(self.x, self.y, self.z)

    def rotateAxes(self) -> 'Vector':
        tmp = self.z
        self.z = self.y
        self.y = self.x
        self.x = tmp
        return self

    def turnAroundX90(self) -> 'Vector':
        tmp = self.y
        self.y = -self.z
        self.z = tmp
        return self

    def turnAroundY90(self) -> 'Vector':
        tmp = self.x
        self.x = self.z
        self.z = -tmp
        return self

    def turnAroundZ90(self) -> 'Vector':
        tmp = self.x
        self.x = -self.y
        self.y = tmp
        return self

    def turnAroundX180(self) -> 'Vector':
        self.y = -self.y
        self.z = -self.z
        return self

    def turnAroundY180(self) -> 'Vector':
        self.x = -self.x
        self.z = -self.z
        return self

    def turnAroundZ180(self) -> 'Vector':
        self.x = -self.x
        self.y = -self.y
        return self

    def reverse(self) -> 'Vector':
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        return self

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'V({self.x}/{self.y}/{self.z})'
