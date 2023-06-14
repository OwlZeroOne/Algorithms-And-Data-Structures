import unittest
import binaryTree as bt

class TestBinaryTree(unittest.TestCase):
    """
    Perform tests on a binary tree.
    """
    def setUp(self) -> None:
        self.bt = bt.BinaryTree(5)

    def test_initialize(self):
        """
        Initialize binary tree of initial size `0` and max size `5`.
        """
        bt = self.bt
        self.assertEqual(bt.size, 0)
        self.assertEqual(bt.maxSize, 5)
        self.assertEqual(bt.toList(), [])


    def test_insertOne(self):
        """
        Insert one item into the binary tree. Final size should be 1 and lookup for the item should be successful with the item being returned.
        """
        bt = self.bt
        bt.insert(9)
        self.assertEqual(bt.size, 1)

        rootKey = bt.root.key
        self.assertEqual(rootKey, 9)

        self.assertEqual(bt.toList(), [9])


    def test_insertToParentWithNoRoot(self):
        """
        Attempt to insert a key to an empty tree given a parent key. `ValueError` should be raised.
        """
        bt = self.bt
        with self.assertRaises(ValueError):
            bt.insert(9,1)


    def test_insertThree(self):
        """
        Insert three keys into the tree. The final tree should have a size of three. 
        """
        # The tree should be of the following format:
        #   9
        #  / \
        # 7   1
        bt = self.bt
        bt.insert(9)
        bt.insert(7, 9)
        bt.insert(1, 9)

        self.assertEqual(bt.size, 3)
        self.assertEqual(bt.root.key, 9)
        self.assertEqual(bt.root.left.key, 7)
        self.assertEqual(bt.root.right.key, 1)
        self.assertEqual(bt.toList(), [7,9,1])


    def test_insertToNonExistentParent(self):
        """
        Attempt to insert a key to a non-existstent parent. Should throw a `LookupError`.
        """
        bt = self.bt
        bt.insert(9)
        
        with self.assertRaises(LookupError):
            bt.insert(7, 1)


    def test_insertToParentWithTwoChildren(self):
        """
        Attempt to insert a new key to a parent that already has left and right children.
        """
        # Try to insert to the root of the following tree:
        #   9
        #  / \
        # 7   1
        bt = self.bt
        bt.insert(9)
        bt.insert(7, 9)
        bt.insert(1, 9)

        with self.assertRaises(ValueError):
            bt.insert(4,9)


    def test_insertExistingKey(self):
        """
        Attempt to insert a key that already exists within the tree. Should throw a `LookupError`.
        """
        bt = self.bt
        bt.insert(9)
        bt.insert(7, 9)
        bt.insert(1, 9)

        with self.assertRaises(LookupError):
            bt.insert(7,1)


    def test_insertToFullTree(self):
        """
        Attempt to insert a new key into a full Tree. An `OverflowError` should be raised.
        """
        bt = self.bt
        bt.insert(9)
        bt.insert(7, 9)
        bt.insert(1, 9)
        bt.insert(2, 1)
        bt.insert(6, 1)

        with self.assertRaises(OverflowError):
            bt.insert(3, 7)


    def test_differentFullTrees(self):
        """
        Test a few different trees.
        """
        #     10
        #    /
        #   7
        #  / \
        # 5   9
        #    /
        #   8
        tree = bt.BinaryTree(5)
        tree.insert(10)
        tree.insert(7,10)
        tree.insert(5,7)
        tree.insert(9,7)
        tree.insert(8,9)

        self.assertEqual(tree.size, 5)
        self.assertEqual(tree.root.key, 10)
        self.assertEqual(tree.toList(), [5,7,8,9,10])

        #   2
        #  / \
        # 1   4
        #    / \
        #   3   5
        tree = bt.BinaryTree(5)
        tree.insert(2)
        tree.insert(1,2)
        tree.insert(4,2)
        tree.insert(3,4)
        tree.insert(5,4)

        self.assertEqual(tree.size, 5)
        self.assertEqual(tree.root.key, 2)
        self.assertEqual(tree.toList(), [1,2,3,4,5])

        #       5
        #      /
        #     4
        #    /
        #   2
        #  / \
        # 1   3
        tree = bt.BinaryTree(5)
        tree.insert(5)
        tree.insert(4,5)
        tree.insert(2,4)
        tree.insert(1,2)
        tree.insert(3,2)

        self.assertEqual(tree.size, 5)
        self.assertEqual(tree.root.key, 5)
        self.assertEqual(tree.toList(), [1,2,3,4,5])


    def test_deleteOneLeaf(self):
        """
        Delete one valid leaf (no children) key from the tree.
        """
        #     3           3
        #    / \         / \
        #   2   5   ->  2   5
        #  /   /           /
        # 1   4           4
        bt = self.bt
        bt.insert(3)
        bt.insert(2, 3)
        bt.insert(5, 3)
        bt.insert(1, 2)
        bt.insert(4, 5)

        self.assertEqual(bt.toList(), [1,2,3,4,5])
        bt.delete(1)

        self.assertEqual(bt.toList(), [2,3,4,5])
        self.assertEqual(bt.size, 4)
        
    
    def test_deleteOneChildParent(self):
        """
        Delete a parent with only a single child from the tree.
        """
        #     3           3
        #    / \         / \
        #   2   5   ->  1   5
        #  /   /           /
        # 1   4           4
        bt = self.bt
        bt.insert(3)
        bt.insert(2, 3)
        bt.insert(5, 3)
        bt.insert(1, 2)
        bt.insert(4, 5)

        self.assertEqual(bt.toList(), [1,2,3,4,5])
        bt.delete(2)

        self.assertEqual(bt.toList(), [1,3,4,5])
        self.assertEqual(bt.size, 4)


    def test_deleteTwoChildParent(self):
        """
        Delete a parent with two children from the tree.
        """
        #     3             5
        #    / \           / \
        #   2   5   ->    2   4
        #  /   /         / 
        # 1   4         1
        bt = self.bt
        bt.insert(3)
        bt.insert(2, 3)
        bt.insert(5, 3)
        bt.insert(1, 2)
        bt.insert(4, 5)

        self.assertEqual(bt.toList(), [1,2,3,4,5])
        bt.delete(3)

        self.assertEqual(bt.toList(), [1,2,5,4])
        self.assertEqual(bt.size, 4)

    
    def test_deleteNonExistentKey(self):
        """
        Attempt to remove a key that does not exist from the tree. Should throw a `LookupError` exception.
        """
        bt = self.bt
        bt.insert(3)
        bt.insert(2, 3)
        bt.insert(5, 3)

        self.assertEqual(bt.toList(), [2,3,5])
        with self.assertRaises(LookupError):
            bt.delete(4)


    def test_deleteFromEmptyTree(self):
        """
        Attempt to delete from an empty tree. Should throw a `LookupError` exception.
        """
        bt = self.bt
        with self.assertRaises(LookupError):
            bt.delete(1)


    def test_treeHeight(self):
        """
        Check tree heights of three different trees. A Tree height is the maximum number of edges from the root to any leaf node in either of subtrees.
        """
        #     1
        #    / \
        #   2   3
        #  / |  |
        # 4  5  6
        # HEIGHT =  2
        tree = bt.BinaryTree(6)
        tree.insert(1)
        tree.insert(2,1)
        tree.insert(3,1)
        tree.insert(4,2)
        tree.insert(5,2)
        tree.insert(6,3)

        self.assertEqual(tree.toList(), [4,2,5,1,6,3])
        self.assertEqual(tree.height(), 2)

        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        #    / \
        #   6   7
        # HEIGHT = 3
        tree = bt.BinaryTree(7)
        tree.insert(1)
        tree.insert(2,1)
        tree.insert(3,1)
        tree.insert(4,2)
        tree.insert(5,2)
        tree.insert(6,5)
        tree.insert(7,5)

        self.assertEqual(tree.toList(), [4,2,6,5,7,1,3])
        self.assertEqual(tree.height(), 3)

        #     _1_
        #    /   \
        #   2     3
        #  / \   / \
        # 4   5 6   7
        #      / \
        #     8   9
        #    /
        #   10
        #  /  \
        # 11   12
        #     /  \
        #   13   14
        #        /
        #       15
        # HEIGHT = 7
        tree = bt.BinaryTree(15)
        tree.insert(1)
        tree.insert(2,1)
        tree.insert(3,1)
        tree.insert(4,2)
        tree.insert(5,2)
        tree.insert(6,3)
        tree.insert(7,3)
        tree.insert(8,6)
        tree.insert(9,6)
        tree.insert(10,8)
        tree.insert(11,10)
        tree.insert(12,10)
        tree.insert(13,12)
        tree.insert(14,12)
        tree.insert(15,14)

        self.assertEqual(tree.toList(), [4,2,5,1,11,10,13,12,15,14,8,6,9,3,7])
        self.assertEqual(tree.height(), 7)


    def test_heightOfEmptyTree(self):
        """
        Return 0 for the height of an empty tree.
        """
        bt = self.bt
        self.assertEqual(bt.height(), 0)


    def test_heightOfNode(self):
        """
        Find and return the height of the node of provided key. Height of a node is the maximum number of edges from the node to any leaf in its subtree.
        """
        #     _1_
        #    /   \
        #   2     3
        #  / \   / \
        # 4   5 6   7
        #      / \
        #     8   9
        #    /
        #   10
        #  /  \
        # 11   12
        #     /  \
        #   13   14
        #        /
        #       15
        tree = bt.BinaryTree(15)
        tree.insert(1)
        tree.insert(2,1)
        tree.insert(3,1)
        tree.insert(4,2)
        tree.insert(5,2)
        tree.insert(6,3)
        tree.insert(7,3)
        tree.insert(8,6)
        tree.insert(9,6)
        tree.insert(10,8)
        tree.insert(11,10)
        tree.insert(12,10)
        tree.insert(13,12)
        tree.insert(14,12)
        tree.insert(15,14)

        self.assertEqual(tree.heightOf(1), 7)
        self.assertEqual(tree.heightOf(2), 1)
        self.assertEqual(tree.heightOf(6), 5)
        self.assertEqual(tree.heightOf(9), 0)
        self.assertEqual(tree.heightOf(13), 0)
        self.assertEqual(tree.heightOf(14), 1)


    def test_heightOfNonExistentNode(self):
        """
        Attempt to find the height of a node that does not exist. A `LookupError` should be raised.
        """
        bt = self.bt
        bt.insert(3)
        bt.insert(2, 3)
        bt.insert(5, 3)

        with self.assertRaises(LookupError):
            bt.heightOf(7)


    def test_depthOfNode(self):
        """
        Find and return the depth of a given node. A node depth is the number of edges from the node to the root node.
        """
        #     _1_
        #    /   \
        #   2     3
        #  / \   / \
        # 4   5 6   7
        #      / \
        #     8   9
        #    /
        #   10
        #  /  \
        # 11   12
        #     /  \
        #   13   14
        #        /
        #       15
        tree = bt.BinaryTree(15)
        tree.insert(1)
        tree.insert(2,1)
        tree.insert(3,1)
        tree.insert(4,2)
        tree.insert(5,2)
        tree.insert(6,3)
        tree.insert(7,3)
        tree.insert(8,6)
        tree.insert(9,6)
        tree.insert(10,8)
        tree.insert(11,10)
        tree.insert(12,10)
        tree.insert(13,12)
        tree.insert(14,12)
        tree.insert(15,14)

        self.assertEqual(tree.depthOf(14), 6)
        self.assertEqual(tree.depthOf(11), 5)
        self.assertEqual(tree.depthOf(8), 3)
        self.assertEqual(tree.depthOf(9), 3)
        self.assertEqual(tree.depthOf(4), 2)
        self.assertEqual(tree.depthOf(1), 0)


    def test_depthOfNonExistentNode(self):
        """
        Attempt to find the depth of a node that does not exist. A `LookupError` should be raised.
        """
        bt = self.bt
        bt.insert(3)
        bt.insert(2, 3)
        bt.insert(5, 3)

        with self.assertRaises(LookupError):
            bt.depthOf(9)


import bst

class TestBinarySearchTree(unittest.TestCase):
    # This test works with the following tree:
    #
    #           47
    #          /  \
    #        12    54
    #       /  |     \
    #     10   33     89
    #         / |     | \
    #       24  42    76 90
    #
    # The tree is implied by `setUp()`
    def setUp(self) -> None:
        "This setup already tests the `insert()` function."
        tree = self.bst = bst.BinarySearchTree(10)
        tree.insert(47)
        tree.insert(12)
        tree.insert(54)
        tree.insert(10)
        tree.insert(33)
        tree.insert(42)
        tree.insert(89)
        tree.insert(76)
        tree.insert(90)
        tree.insert(24)


    def test_initialize(self):
        """
        Test the initial state of the BST. Because `BinarySearchTree` inherits from `BinaryTree`, we need not to test unchanged functions and can reuse them to test functions here.
        """
        tree = self.bst
        self.assertEqual(tree.root.key, 47)
        self.assertEqual(tree.height(), 3)
        self.assertEqual(tree.size, 10)
        self.assertEqual(tree.toList(),[10,12,24,33,42,47,54,76,89,90])


    def test_deleteLeaf(self):
        """
        Attempt to delete a leaf node that exists within the tree. The output should be a tree reorganized to maintain the BST property.
        """
        # Removing 42 should give
        #
        #           47
        #          /  \
        #        12    54
        #       /  |     \
        #     10   33     89
        #          |      | \
        #          24     76 90
        #
        tree = self.bst
        tree.delete(42)

        self.assertEqual(tree.size, 9)
        self.assertEqual(tree.toList(), [10,12,24,33,47,54,76,89,90])


    def test_deleteOneChildParent(self):
        """
        Attempt to remove a node which consists of only one child node.
        """
        # Removing 54 should result in
        #
        #           47
        #          /  \
        #        12    89
        #       /  |   | \
        #     10   33  76 90
        #         / |     
        #       24  42    
        #
        tree = self.bst
        tree.delete(54)

        self.assertEqual(tree.size, 9)
        self.assertEqual(tree.toList(),[10,12,24,33,42,47,76,89,90])


    def test_deleteTwoChildrenParent(self):
        """
        Attempt to remove a node which consists of two child nodes.
        """
        # Removing 12 should leave the tree with
        #
        #           47
        #          /  \
        #        24    54
        #       / |      \
        #     10  33      89
        #         |       | \
        #         42      76 90
        #
        tree = self.bst
        tree.delete(12)

        self.assertEqual(tree.size, 9)
        self.assertEqual(tree.toList(),[10,24,33,42,47,54,76,89,90])


    def test_deleteRootWithTwoChildren(self):
        """
        Attempt to remove the root node which consists of two children.
        """
        # Removing 47 should leave the tree with
        #
        #           54
        #          /  \
        #        12    89
        #       /  |   | \
        #     10   33  76 90
        #         / |   
        #       24  42 
        #
        tree = self.bst
        tree.delete(47)

        self.assertEqual(tree.size, 9)
        self.assertEqual(tree.toList(),[10,12,24,33,42,54,76,89,90])


    def test_deleteMany(self):
        """
        Attempt do delete a few nodes from the tree.
        """
        # Initial state:
        #
        #           47
        #          /  \
        #        12    54
        #       /  |     \
        #     10   33     89
        #         / |     | \
        #       24  42    76 90
        #
        tree = self.bst
        tree.delete(12)
        tree.delete(33)
        tree.delete(89)
        tree.delete(47)
        # Final state:
        #
        #           54
        #          /  \
        #        24    90
        #       /  |   |
        #     10   42  76
        #                 
        self.assertEqual(tree.size, 6)
        self.assertEqual(tree.toList(), [10,24,42,54,76,90])


    def test_deleteNonExistentNode(self):
        """
        Attempt to remove a non-existent node from a populated tree. Should raise a `RuntimeError` exception.
        """
        tree = self.bst
        with self.assertRaises(RuntimeError):
            bst.delete(4)


class TestAVL(unittest.TestCase):
    pass


class TestHeap(unittest.TestCase):
    pass


class TestRB(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()