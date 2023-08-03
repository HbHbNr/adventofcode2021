"""Unit tests for https://adventofcode.com/2021/day/18 part a"""
import unittest
from days import day18a
from util import tokenstream


class TestDay18a(unittest.TestCase):

    def testTokenListToString(self):
        string = '[9,[8,7]]'
        tokenList = tokenstream.TokenStream(string).asList()

        assert day18a.MathHomework.tokenListToString(tokenList) == string

    def testExampleReduce(self):
        for originalString, explodedString in [
                    ('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'),
                    ('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'),
                    ('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'),
                    ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
                    ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
                ]:
            tokenList = tokenstream.TokenStream(originalString).asList()
            exploded = day18a.MathHomework.tryExplode(tokenList)

            assert exploded is True
            assert day18a.MathHomework.tokenListToString(tokenList) == explodedString

    def testInput(self) -> None:
        # assert a = b
        pass
