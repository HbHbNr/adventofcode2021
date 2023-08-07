"""Unit tests for https://adventofcode.com/2021/day/18 part a"""
import unittest
from typing import List
from days import day18a
from util import tokenstream

# typing.TypeAlias needs at least Python 3.10, so no type hints
Token = tokenstream.Token
TokenStream = tokenstream.TokenStream


class TestDay18a(unittest.TestCase):

    def testReadTokenFile1(self) -> None:
        tokenListList = day18a.MathHomework.readTokenFile('inputfiles/day18_example1.txt')
        tokenList = day18a.MathHomework.addAndReduce(tokenListList)

        assert day18a.MathHomework.tokenListToString(tokenList) == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'

    def testReadTokenFile2(self) -> None:
        tokenListList = day18a.MathHomework.readTokenFile('inputfiles/day18_example2.txt')
        tokenList = day18a.MathHomework.addAndReduce(tokenListList)
        magnitude = day18a.MathHomework.calcMagnitude(token for token in tokenList)

        assert magnitude == 4140

    def testCalcMagnitude(self) -> None:
        for originalString, magnitude in [
                    ('[[1,2],[[3,4],5]]', 143),
                    ('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 1384),
                    ('[[[[1,1],[2,2]],[3,3]],[4,4]]', 445),
                    ('[[[[3,0],[5,3]],[4,4]],[5,5]]', 791),
                    ('[[[[5,0],[7,4]],[5,5]],[6,6]]', 1137),
                    ('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 3488)
                ]:
            tokenStream = TokenStream(originalString).stream()
            magnitude2 = day18a.MathHomework.calcMagnitude(tokenStream)

            assert magnitude2 == magnitude

    def testExampleAddAndReduce(self) -> None:
        tokenListList: List[List[Token]] = []
        for originalString in ['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]', '[6,6]']:
            tokenListList.append(TokenStream(originalString).asList())
        result = day18a.MathHomework.addAndReduce(tokenListList)

        assert day18a.MathHomework.tokenListToString(result) == '[[[[5,0],[7,4]],[5,5]],[6,6]]'

    def testExampleTryExplode(self) -> None:
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

    def testExampleTrySplit(self) -> None:
        for originalString, splitString, splitHappened in [
                    ('5', '5', False),
                    ('[5]', '[5]', False),
                    ('15', '[7,8]', True),
                    ('[1,15]', '[1,[7,8]]', True),
                    ('19', '[9,10]', True),
                    ('[9,10]', '[9,[5,5]]', True)
                ]:
            tokenList = TokenStream(originalString).asList()
            split = day18a.MathHomework.trySplit(tokenList)

            assert split is splitHappened
            assert day18a.MathHomework.tokenListToString(tokenList) == splitString

    def testExampleTryReduce(self) -> None:
        for originalString, reducedString in [
                    ('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
                ]:
            tokenList = TokenStream(originalString).asList()
            tokenListReduced = day18a.MathHomework.reduce(tokenList)

            assert day18a.MathHomework.tokenListToString(tokenListReduced) == reducedString

    def testTokenListToString(self) -> None:
        string = '[9,[8,7]]'
        tokenList = TokenStream(string).asList()

        assert day18a.MathHomework.tokenListToString(tokenList) == string

    def testInput(self) -> None:
        tokenListList = day18a.MathHomework.readTokenFile('inputfiles/day18_input.txt')
        tokenList = day18a.MathHomework.addAndReduce(tokenListList)
        magnitude = day18a.MathHomework.calcMagnitude(token for token in tokenList)

        assert magnitude == 3551
