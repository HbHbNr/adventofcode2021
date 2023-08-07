"""Unit tests for the TreeNode class"""
import unittest
from util import tokenstream, binarytree


class TestTreeNode(unittest.TestCase):

    def testExample12(self):
        treeNode = binarytree.TreeNode.createParents(binarytree.TreeNode.createLeaf(1),
                                                     binarytree.TreeNode.createLeaf(2))

        assert str(treeNode) == '[1,2]'

    def testExample123(self):
        treeNode1 = binarytree.TreeNode.createParents(binarytree.TreeNode.createLeaf(1),
                                                      binarytree.TreeNode.createLeaf(2))
        treeNode2 = binarytree.TreeNode.createParents(treeNode1,
                                                      binarytree.TreeNode.createLeaf(3))

        assert str(treeNode2) == '[[1,2],3]'

    def testExampleTokenStream12(self):
        tokenStream = tokenstream.TokenStream('[1,2]').stream()
        treeNode = binarytree.TreeNode.parseTokenStream(tokenStream)

        assert str(treeNode) == '[1,2]'

    def testExampleTokenStream123(self):
        tokenStream = tokenstream.TokenStream('[[1,2],3]').stream()
        treeNode = binarytree.TreeNode.parseTokenStream(tokenStream)

        assert str(treeNode) == '[[1,2],3]'

    def testExampleTokenStream987(self):
        tokenStream = tokenstream.TokenStream('[9,[8,7]]').stream()
        treeNode = binarytree.TreeNode.parseTokenStream(tokenStream)

        assert str(treeNode) == '[9,[8,7]]'
