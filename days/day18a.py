"""Solution for https://adventofcode.com/2021/day/18 part a"""
from typing import NamedTuple, Optional, List
from util import util
from util import tokenstream


class TreeNode(NamedTuple):

    left: Optional['TreeNode']
    right: Optional['TreeNode']
    value: int

    @classmethod
    def createParents(cls, left: 'TreeNode', right: 'TreeNode') -> 'TreeNode':
        treeNode = TreeNode(left, right, 0)
        # print("createParents:", treeNode)
        return treeNode

    @classmethod
    def createLeaf(cls, value: int) -> 'TreeNode':
        treeNode = TreeNode(None, None, value)
        # print("createLeaf:", treeNode)
        return treeNode

    @classmethod
    def parseTokenStream(cls, tokenStream) -> 'TreeNode':
        token = next(tokenStream)
        if token.isInteger():
            # the tree node is a single integer
            return TreeNode.createLeaf(token.intvalue)

        # the tree node is a parent node
        left: TreeNode = cls.parseTokenStream(tokenStream)
        _ = next(tokenStream)  # comma
        right: TreeNode = cls.parseTokenStream(tokenStream)
        _ = next(tokenStream)  # closing bracket
        return TreeNode.createParents(left, right)

    def isLeaf(self):
        return self.left is None

    def __str__(self) -> str:
        if self.isLeaf():
            string = str(self.value)
        else:
            string = f'[{str(self.left)},{str(self.right)}]'
        return string


class MathHomework:
    # pylint: disable=too-few-public-methods

    @classmethod
    def reduce(cls, tokens: List[tokenstream.Token]) -> List[tokenstream.Token]:
        _tokens: List[tokenstream.Token] = list(tokens)
        # print(tokens)
        # print(_tokens)

        run = True
        while run:
            if cls._tryExplode(_tokens):
                # continue
                pass
            if cls._trySplit(_tokens):
                continue
            # neither explode nor split was possible: work done
            run = False

        return _tokens

    @classmethod
    def _tryExplode(cls, tokens: List[tokenstream.Token]) -> bool:
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
    def _trySplit(cls, _: List[tokenstream.Token]) -> bool:
        return False


def main():
    # for string in ['[1,2]', '[[1,2],3]', '[9,[8,7]]']:
    #     print('***************', string, '***************')
    #     tokenStream = tokenstream.TokenStream(string).stream()
    #     treeNode = TreeNode.parseTokenStream(tokenStream)
    #     print(treeNode)

    for string in ['[[[[[9,8],1],2],3],4]', '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]']:
        print('***************', string, '***************')
        tokenStream = tokenstream.TokenStream(string).stream()
        tokenList = list(tokenStream)
        tokenList2 = MathHomework.reduce(tokenList)
        for token in tokenList2:
            if token.type is tokenstream.TokenType.INTEGER:
                print(token.intvalue, end='')
            else:
                print(token.type.toString(), end='')
        print()

    util.printresultline('18a', '???')


if __name__ == '__main__':
    main()
