"""A class for matrices"""
from typing import List


class Matrix3x3:

    _aij: List[int]

    def __init__(self, xyz: List[int]) -> None:
        if len(xyz) != 9:
            raise ValueError('intialization list needs to contain 9 integers')
        self._aij = xyz.copy()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'M({}/{}/{} {}/{}/{} {}/{}/{})'.format(*self._aij)  # pylint: disable=consider-using-f-string
