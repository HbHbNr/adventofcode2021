"""Unit tests for https://adventofcode.com/2021/day/18 part b"""
import unittest
from typing import List
import itertools
from days import day18a
from util import tokenstream

# typing.TypeAlias needs at least Python 3.10, so no type hints
Token = tokenstream.Token
TokenStream = tokenstream.TokenStream


class TestDay18a(unittest.TestCase):

    def testExample(self) -> None:
        magnitudes: List[int] = []
        tokenListList = day18a.MathHomework.readTokenFile('inputfiles/day18_example2.txt')
        for pair in itertools.permutations(tokenListList, 2):
            tokenList = day18a.MathHomework.addAndReduce(list(pair))
            magnitude = day18a.MathHomework.calcMagnitude(token for token in tokenList)
            magnitudes.append(magnitude)

        assert max(magnitudes) == 3993

    def testInput(self) -> None:
        magnitudes: List[int] = []
        tokenListList = day18a.MathHomework.readTokenFile('inputfiles/day18_input.txt')
        for pair in itertools.permutations(tokenListList, 2):
            tokenList = day18a.MathHomework.addAndReduce(list(pair))
            magnitude = day18a.MathHomework.calcMagnitude(token for token in tokenList)
            magnitudes.append(magnitude)

        assert max(magnitudes) == 4555
