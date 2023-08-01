"""Unit tests for https://adventofcode.com/2021/day/18 part a"""
import unittest
from days import day18a
from util import tokenstream


class TestDay18a(unittest.TestCase):

    def testExample12(self):
        treeNode = day18a.TreeNode.createParents(day18a.TreeNode.createLeaf(1), day18a.TreeNode.createLeaf(2))

        assert str(treeNode) == '[1,2]'

    def testExample123(self):
        treeNode = \
            day18a.TreeNode.createParents(day18a.TreeNode.createParents(day18a.TreeNode.createLeaf(1),
                                                                        day18a.TreeNode.createLeaf(2)),
                                          day18a.TreeNode.createLeaf(3))

        assert str(treeNode) == '[[1,2],3]'

    def testExampleTokenStream12(self):
        tokenStream = tokenstream.TokenStream('[1,2]').stream()
        treeNode = day18a.TreeNode.parseTokenStream(tokenStream)

        assert str(treeNode) == '[1,2]'

    def testExampleTokenStream123(self):
        tokenStream = tokenstream.TokenStream('[[1,2],3]').stream()
        treeNode = day18a.TreeNode.parseTokenStream(tokenStream)

        assert str(treeNode) == '[[1,2],3]'

    def testExampleTokenStream987(self):
        tokenStream = tokenstream.TokenStream('[9,[8,7]]').stream()
        treeNode = day18a.TreeNode.parseTokenStream(tokenStream)

        assert str(treeNode) == '[9,[8,7]]'

    def testInput(self) -> None:
        # assert a = b
        pass
