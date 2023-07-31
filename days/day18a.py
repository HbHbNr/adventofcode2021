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
        return TreeNode(left, right, 0)

    @classmethod
    def createLeaf(cls, value: int) -> 'TreeNode':
        return TreeNode(None, None, value)

    def isLeaf(self):
        return self.left is None

    def __str__(self) -> str:
        if self.isLeaf():
            string = str(self.value)
        else:
            string = f'[{str(self.left)},{str(self.right)}]'
        return string


def main():
    token = tokenstream.Token.createInteger(3)
    print(token)
    token = tokenstream.Token.createBasic(',')
    print(token)
    treeNode = TreeNode.createParents(TreeNode.createLeaf(1), TreeNode.createLeaf(2))
    print(treeNode)

    util.printresultline('18a', '???')


if __name__ == '__main__':
    main()
