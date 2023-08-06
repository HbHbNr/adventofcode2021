"""Solution for https://adventofcode.com/2021/day/18 part a"""
from typing import List
import math
from util import util
from util import tokenstream

# typing.TypeAlias needs at least Python 3.10, so no type hints
Token = tokenstream.Token
TokenList = List[Token]
TokenType = tokenstream.TokenType
TokenStream = tokenstream.TokenStream


class MathHomework:

    @classmethod
    def calcMagnitude(cls, tokenStream) -> int:
        token: Token = next(tokenStream)
        if token.isInteger():
            # the tree node is a single integer
            return token.intvalue

        # the tree node is a parent node
        leftValue: int = cls.calcMagnitude(tokenStream)
        _ = next(tokenStream)  # comma
        rightValue: int = cls.calcMagnitude(tokenStream)
        _ = next(tokenStream)  # closing bracket
        return 3 * leftValue + 2 * rightValue

    @classmethod
    def addAndReduce(cls, tokenListList: List[TokenList]) -> TokenList:
        result = tokenListList[0]
        for i in range(1, len(tokenListList)):
            nextPart = tokenListList[i]
            result = cls.createPair(result, nextPart)
            result = cls.reduce(result)
        return result

    @classmethod
    def createPair(cls, left: TokenList, right: TokenList) -> TokenList:
        tokenList: List[Token] = []
        tokenList.append(Token.createBasic('['))
        tokenList.extend(left)
        tokenList.append(Token.createBasic(','))
        tokenList.extend(right)
        tokenList.append(Token.createBasic(']'))
        return tokenList

    @classmethod
    def reduce(cls, tokens: TokenList) -> TokenList:
        _tokens: TokenList = list(tokens)

        run = True
        while run:
            if cls.tryExplode(_tokens):
                continue
            if cls.trySplit(_tokens):
                continue
            # neither explode nor split was possible: work done
            run = False

        return _tokens

    @classmethod
    def tryExplode(cls, tokens: TokenList) -> bool:
        exploded = False
        i = 0
        level = 0
        for i, token in enumerate(tokens):
            if token.type == TokenType.SQUARE_BRACKET_OPEN:
                level += 1
            elif token.type == TokenType.SQUARE_BRACKET_CLOSE:
                level -= 1
            if level == 5:
                exploded = True
                break  # i and token keep their values
        # found pair at level 5
        if exploded:
            left = tokens[i + 1]
            right = tokens[i + 3]
            del tokens[i + 1:i + 5]
            tokens[i] = Token.createInteger(0)
            # add left.intValue to first number on left side
            for j in range(i - 1, -1, -1):
                if tokens[j].type == TokenType.INTEGER:
                    tokens[j] = Token.createInteger(tokens[j].intvalue + left.intvalue)
                    break
            # add right.intValue to first number on right side
            for j in range(i + 1, len(tokens)):
                if tokens[j].type == TokenType.INTEGER:
                    tokens[j] = Token.createInteger(tokens[j].intvalue + right.intvalue)
                    break
        return exploded

    @classmethod
    def trySplit(cls, tokens: TokenList) -> bool:
        split = False
        i = 0
        for i, token in enumerate(tokens):
            if token.type == TokenType.INTEGER:
                if token.intvalue >= 10:
                    split = True
                    break  # i and token keep their values
        # found regular number 10 or greater
        if split:
            leftInt: int = math.floor(tokens[i].intvalue / 2)
            rightInt: int = math.ceil(tokens[i].intvalue / 2)
            del tokens[i]
            tokens.insert(i + 0, Token.createBasic('['))
            tokens.insert(i + 1, Token.createInteger(leftInt))
            tokens.insert(i + 2, Token.createBasic(','))
            tokens.insert(i + 3, Token.createInteger(rightInt))
            tokens.insert(i + 4, Token.createBasic(']'))
        return split

    @classmethod
    def tokenListToString(cls, tokens: TokenList) -> str:
        stringList: List[str] = []
        for token in tokens:
            if token.type is TokenType.INTEGER:
                stringList.append(str(token.intvalue))
            else:
                stringList.append(token.type.toString())
        return ''.join(stringList)


def main():
    # for string in ['[1,2]', '[[1,2],3]', '[9,[8,7]]']:
    #     print('***************', string, '***************')
    #     tokenStream = tokenstream.TokenStream(string).stream()
    #     treeNode = TreeNode.parseTokenStream(tokenStream)
    #     print(treeNode)

    for string in ['[[[[[9,8],1],2],3],4]', '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]']:
        print('***************', string, '***************')
        tokenList = tokenstream.TokenStream(string).asList()
        tokenListReduced = MathHomework.reduce(tokenList)
        for token in tokenListReduced:
            if token.type is TokenType.INTEGER:
                print(token.intvalue, end='')
            else:
                print(token.type.toString(), end='')
        print()

    tokenList = [Token.createInteger(19)]
    print(MathHomework.tokenListToString(tokenList))
    tokenListReduced = MathHomework.reduce(tokenList)
    print(MathHomework.tokenListToString(tokenListReduced))

    tokenList1 = TokenStream('[1,1]').asList()
    tokenList2 = TokenStream('[2,3]').asList()
    result = MathHomework.addAndReduce([tokenList1, tokenList2])
    print(MathHomework.tokenListToString(result))

    util.printresultline('18a', '???')


if __name__ == '__main__':
    main()
