"""A class for vectors"""


class Vector:

    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def rotateAxes(self) -> None:
        tmp = self.z
        self.z = self.y
        self.y = self.x
        self.x = tmp

    def turnAroundX90(self) -> None:
        tmp = self.y
        self.y = -self.z
        self.z = tmp

    def turnAroundY90(self) -> None:
        tmp = self.x
        self.x = self.z
        self.z = -tmp

    def turnAroundZ90(self) -> None:
        tmp = self.x
        self.x = -self.y
        self.y = tmp

    def turnAroundX180(self) -> None:
        self.y = -self.y
        self.z = -self.z

    def turnAroundY180(self) -> None:
        self.x = -self.x
        self.z = -self.z

    def turnAroundZ180(self) -> None:
        self.x = -self.x
        self.y = -self.y

    def reverse(self) -> None:
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'V({self.x}/{self.y}/{self.z})'
