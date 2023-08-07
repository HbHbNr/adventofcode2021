"""Classes for binary trees"""
from typing import NamedTuple, Optional


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
