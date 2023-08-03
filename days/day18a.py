"""Solution for https://adventofcode.com/2021/day/18 part a"""
from typing import List
from util import util
from util import tokenstream

# typing.TypeAlias needs at least Python 3.10
TokenList = List[tokenstream.Token]


class MathHomework:
    # pylint: disable=too-few-public-methods

    @classmethod
    def reduce(cls, tokens: TokenList) -> TokenList:
        _tokens: TokenList = list(tokens)
        # print(tokens)
        # print(_tokens)

        run = True
        while run:
            if cls.tryExplode(_tokens):
                # continue
                pass
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
            if token.type == tokenstream.TokenType.SQUARE_BRACKET_OPEN:
                level += 1
            elif token.type == tokenstream.TokenType.SQUARE_BRACKET_CLOSE:
                level -= 1
            if level == 5:
                break  # i and token keep their values
        # pair at level 5 found
        if level == 5:
            left = tokens[i + 1]
            right = tokens[i + 3]
            del tokens[i + 1:i + 5]
            tokens[i] = tokenstream.Token.createInteger(0)
            # add left.intValue to first number on left side
            for j in range(i - 1, -1, -1):
                if tokens[j].type == tokenstream.TokenType.INTEGER:
                    tokens[j] = tokenstream.Token.createInteger(tokens[j].intvalue + left.intvalue)
                    break
            # add right.intValue to first number on right side
            for j in range(i + 1, len(tokens)):
                if tokens[j].type == tokenstream.TokenType.INTEGER:
                    tokens[j] = tokenstream.Token.createInteger(tokens[j].intvalue + right.intvalue)
                    break
            exploded = True
        return exploded

    @classmethod
    def trySplit(cls, _: TokenList) -> bool:
        return False

    @classmethod
    def tokenListToString(cls, tokens: TokenList) -> str:
        stringList: List[str] = []
        for token in tokens:
            if token.type is tokenstream.TokenType.INTEGER:
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
            if token.type is tokenstream.TokenType.INTEGER:
                print(token.intvalue, end='')
            else:
                print(token.type.toString(), end='')
        print()

    util.printresultline('18a', '???')


if __name__ == '__main__':
    main()
