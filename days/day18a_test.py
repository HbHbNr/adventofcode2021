"""Unit tests for https://adventofcode.com/2021/day/18 part a"""
import unittest
from days import day18a
from util import tokenstream

# typing.TypeAlias needs at least Python 3.10, so no type hints
TokenStream = tokenstream.TokenStream


class TestDay18a(unittest.TestCase):

    def testTokenListToString(self):
        string = '[9,[8,7]]'
        tokenList = TokenStream(string).asList()

        assert day18a.MathHomework.tokenListToString(tokenList) == string

    def testExampleTryExplode(self):
        for originalString, explodedString in [
                    ('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'),
                    ('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'),
                    ('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'),
                    ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
                    ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
                ]:
            tokenList = TokenStream(originalString).asList()
            exploded = day18a.MathHomework.tryExplode(tokenList)

            assert exploded is True
            assert day18a.MathHomework.tokenListToString(tokenList) == explodedString

    def testExampleTrySplit(self):
        for originalString, splitString, result in [
                    ('5', '5', False),
                    ('[5]', '[5]', False),
                    ('15', '[7,8]', True),
                    ('[1,15]', '[1,[7,8]]', True),
                    ('19', '[9,10]', True),
                    ('[9,10]', '[9,[5,5]]', True)
                ]:
            tokenList = TokenStream(originalString).asList()
            split = day18a.MathHomework.trySplit(tokenList)

            assert split is result
            assert day18a.MathHomework.tokenListToString(tokenList) == splitString

    def testExampleTryReduce(self):
        for originalString, reducedString in [
                    ('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
                ]:
            tokenList = TokenStream(originalString).asList()
            tokenListReduced = day18a.MathHomework.reduce(tokenList)

            assert day18a.MathHomework.tokenListToString(tokenListReduced) == reducedString

    def testInput(self) -> None:
        # assert a = b
        pass
