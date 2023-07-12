from typing import NamedTuple, Optional
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


if __name__ == '__main__':
    from days import util
    token = tokenstream.Token.createInteger(3)

    # solved with https://github.com/HbHbNr/a-star
    util.printresultline('18a', 0)
