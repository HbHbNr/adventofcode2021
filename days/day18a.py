"""Solution for https://adventofcode.com/2021/day/18 part a"""
from typing import NamedTuple, Optional
from util import util
from util import tokenstream


class TreeNode(NamedTuple):

    left: Optional['TreeNode']
    right: Optional['TreeNode']
    value: int

    @classmethod
    def createParent(cls, left: 'TreeNode', right: 'TreeNode') -> 'TreeNode':
        return TreeNode(left, right, 0)

    @classmethod
    def createLeaf(cls, value: int) -> 'TreeNode':
        return TreeNode(None, None, value)

    def isLeaf(self):
        return self.left is not None


def main():
    token = tokenstream.Token.createInteger(3)
    print(token)

    util.printresultline('18a', '???')


if __name__ == '__main__':
    main()
