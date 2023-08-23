"""A class for matrices"""
from typing import NamedTuple


class Matrix3x3(NamedTuple):

    a11: int
    a12: int
    a13: int
    a21: int
    a22: int
    a23: int
    a31: int
    a32: int
    a33: int

    # def __init__(self, aij: Iterable[int]) -> None:
    #     self.aij = tuple(aij)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'M({self.a11}/{self.a12}/{self.a13} {self.a21}/{self.a22}/{self.a23} {self.a31}/{self.a32}/{self.a33})'
