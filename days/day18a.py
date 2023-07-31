"""Solution for https://adventofcode.com/2021/day/18 part a"""
from typing import NamedTuple, Optional
from util import util
from util import tokenstream


class TreeNode(NamedTuple):

    left: Optional['TreeNode']
    right: Optional['TreeNode']
    value: int

    @classmethod
    def createParents(cls, left: 'TreeNode', right: 'TreeNode') -> 'TreeNode':
        treeNode = TreeNode(left, right, 0)
        print("createParents:", treeNode)
        return treeNode

    @classmethod
    def createLeaf(cls, value: int) -> 'TreeNode':
        treeNode = TreeNode(None, None, value)
        print("createLeaf:", treeNode)
        return treeNode

    @classmethod
    def parseTokenStream(cls, tokenStream) -> 'TreeNode':
        token = next(tokenStream)
        if token.isInteger():
            return TreeNode.createLeaf(token.intvalue)
        left: 'TreeNode' = cls.parseTokenStream(tokenStream)
        _ = next(tokenStream)  # comma
        token = next(tokenStream)
        if token.isInteger():
            right = TreeNode.createLeaf(token.intvalue)
        else:
            right = cls.parseTokenStream(tokenstream)  # first token already consumed!!!
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


def main():
    for string in ['[1,2]', '[[1,2],3]']:
        tokenStream = tokenstream.TokenStream(string).stream()
        treeNode = TreeNode.parseTokenStream(tokenStream)
        print(treeNode)

    util.printresultline('18a', '???')


if __name__ == '__main__':
    main()
