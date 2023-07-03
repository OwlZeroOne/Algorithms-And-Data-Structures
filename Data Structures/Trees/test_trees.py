import unittest
import binaryTree as bt
import binarySearchTree as bst
import avlTree as avl

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

        self.assertEqual(tree.heightOfKey(1), 7)
        self.assertEqual(tree.heightOfKey(2), 1)
        self.assertEqual(tree.heightOfKey(6), 5)
        self.assertEqual(tree.heightOfKey(9), 0)
        self.assertEqual(tree.heightOfKey(13), 0)
        self.assertEqual(tree.heightOfKey(14), 1)


    def test_heightOfNonExistentNode(self):
        """
        Attempt to find the height of a node that does not exist. A `LookupError` should be raised.
        """
        bt = self.bt
        bt.insert(3)
        bt.insert(2, 3)
        bt.insert(5, 3)

        with self.assertRaises(LookupError):
            bt.heightOfKey(7)


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
            tree.delete(4)


    def test_validLookup(self):
        """
        Search for a node that exists within the list. Test on four different cases that exist within the tree.
        """
        t1 = 33
        t2 = 76
        t3 = 47
        t4 = 10

        bst = self.bst
        node = bst.lookup(t1)
        self.assertEqual(node.key, t1)

        node = bst.lookup(t2)
        self.assertEqual(node.key, t2)

        node = bst.lookup(t3)
        self.assertEqual(node.key, t3)

        node = bst.lookup(t4)
        self.assertEqual(node.key, t4)


    def test_invalidLookup(self):
        """
        Attempt to find a node that does not exist within the tree. Should throw a `RuntimeError` exception.
        """
        t = 4
        bst = self.bst
        
        with self.assertRaises(RuntimeError):
            bst.lookup(t)


    def test_findMaximum(self):
        """
        Find and return the node with the greatest key.
        """
        bst = self.bst
        max = bst.maximum()

        self.assertEqual(max.key, 90)


    def test_findMinimum(self):
        """
        Find and return the node with the smallest key.
        """
        bst = self.bst
        min = bst.minimum()

        self.assertEqual(min.key, 10)


    def test_deleteNodeFromAnEmptyTree(self):
        """
        Attempt to remove a node from an empty tree. A `RuntimeError` exception should be thrown.
        """
        with self.assertRaises(RuntimeError):
            self.bst.delete(45)


    def test_orderWalks(self):
        """
        Check whether the different walks output appropriate lists.
        """
        # Test tree:
        #         _8_
        #        /   \
        #       5     10
        #      / \    / 
        #     4   6  9
        #    /
        #   2
        #  / \
        # 1   3
        tree = bst.BinarySearchTree(10)
        tree.insert(8)
        tree.insert(5)
        tree.insert(10)
        tree.insert(4)
        tree.insert(6)
        tree.insert(9)
        tree.insert(2)
        tree.insert(1)
        tree.insert(3)

        self.assertEqual(tree.toList("inorder"), [1,2,3,4,5,6,8,9,10])
        self.assertEqual(tree.toList("preorder"), [8,5,4,2,1,3,6,10,9])
        self.assertEqual(tree.toList("postorder"), [1,3,2,4,6,5,9,10,8])


    def test_unbalancedTree(self):
        """
        Test an unbalanced tree to see if it is unbalanced or not.
        """
        # Test tree:
        #         _8_
        #        /   \
        #       5     10
        #      / \    / 
        #     4   6  9
        #    /
        #   2
        #  / \
        # 1   3

        tree = bst.BinarySearchTree(10)
        tree.insert(8)
        tree.insert(5)
        tree.insert(10)
        tree.insert(4)
        tree.insert(6)
        tree.insert(9)
        tree.insert(2)
        tree.insert(1)
        tree.insert(3)

        self.assertFalse(tree.isBalanced())


    def test_balancedTree(self) -> bool:
        """
        Test a balanced tree to see if it is unbalanced or not.
        """
        # Test tree:
        #         _7_
        #        /   \
        #       5     10
        #      / \    / \
        #     3   6  9   11
        #    /      /
        #   2      8 
        #  /
        # 1
        tree = bst.BinarySearchTree(10)
        tree.insert(7)
        tree.insert(5)
        tree.insert(10)
        tree.insert(3)
        tree.insert(6)
        tree.insert(9)
        tree.insert(11)
        tree.insert(8)
        tree.insert(2)
        tree.insert(1)

        self.assertTrue(tree.isBalanced())


    def test_perfectlyBalancedTree(self):
        """
        Test a perfectly balanced tree to see if it is indeed blanaced perfectly or not.
        """
        #TODO
        pass


class TestAVL(unittest.TestCase):
    
    def setUp(self) -> None:
        self.tree = avl.AvlTree(15)


    def test_initialize(self):
        """
        Test initial state of an empty AVL tree. SHould be empty with size 0.
        """
        t = self.tree
        self.assertEqual(t.size, 0)
        self.assertTrue(t.isEmpty())
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 0)


    def test_addOne(self):
        """
        Add one element into the tree. The element should become the root, and the tree should be balanced and not empty.
        """
        t = self.tree
        t.insert(56)
        self.assertEqual(t.size, 1)
        self.assertFalse(t.isEmpty())
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 0) # No edges in the tree, hence height is zero.
        self.assertEqual(t.root.key, 56)


    def test_simpleRightRotation(self):
        """
        Populate the tree with three nodes containing the following keys respectively: 73,71,67. This will test the right rotation algorithm for right skewed trees. Output of preorder list should be `[71,67,73]`.
        """
        # TREE REPRESENTATION
        #
        #       73      ->         71
        #      /                  /  \
        #    71         ->      67    73
        #   /
        # 67            ->
        t = self.tree
        t.insert(73)
        t.insert(71)
        t.insert(67)

        self.assertEqual(t.size, 3)
        self.assertEqual(t.toList("preorder"), [71,67,73])
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 1)


    def test_simpleLeftRotation(self):
        """
        Populate the tree with three nodes containing the following keys respectively: 84,87,88. This will test the left rotation algorithm for left skewed trees. Output of preorder list should be `[87,84,88]`.
        """
        # TREE REPRESENTATION
        #
        # 84            ->         87
        #   \                     /  \
        #    87         ->      84    88
        #      \
        #       88      ->
        t = self.tree
        t.insert(84)
        t.insert(87)
        t.insert(88)

        self.assertEqual(t.size, 3)
        self.assertEqual(t.toList("preorder"), [87,84,88])
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 1)


    def test_simpleLeftRightRotation(self):
        """
        Populate the tree with three nodes containing the following keys respectively: 73,71,72. This will test the left-right rotation algorithm for "left-arrow" trees. Output of preorder list should be `[71,67,73]`.
        """
        # TREE REPRESENTATION
        #
        #    73      ->         72
        #   /                  /  \
        # 71         ->      71    73
        #   \
        #    72      ->
        t = self.tree
        t.insert(73)
        t.insert(71)
        t.insert(72)

        self.assertEqual(t.size, 3)
        self.assertEqual(t.toList("preorder"), [72,71,73])
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 1)


    def test_simpleRightLeftRotation(self):
        """
        Populate the tree with three nodes containing the following keys respectively: 84,87,86. This will test the right-left rotation algorithm for "right-arrow" trees. Output of preorder list should be `[86,84,87]`.
        """
        # TREE REPRESENTATION
        #
        # 84            ->         86
        #   \                     /  \
        #    87         ->      84    87
        #   /
        # 86            ->
        t = self.tree
        t.insert(84)
        t.insert(87)
        t.insert(86)

        self.assertEqual(t.size, 3)
        self.assertEqual(t.toList("preorder"), [86,84,87])
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 1)


    def test_rightRotationOnLargeTree(self):
        # TREE REPRESENTATION
        #
        #          _95_             ->
        #         /    \
        #       83      97          ->            __83__
        #      /  \    /  \                      /      \
        #    64    84 93  99        ->         64       _95_
        #   /  \     \                        /  \     /    \  
        # 59    73    88            ->       59  73   84    97
        #      /                                 /     \   /  \ 
        #    71                     ->         71      88 93  99
        t = self.tree
        t.insert(95)
        t.insert(83)
        t.insert(97)
        t.insert(64)
        t.insert(84)
        t.insert(96)
        t.insert(99)
        t.insert(59)
        t.insert(73)
        t.insert(88)
        t.insert(71)


        self.assertEqual(t.size, 11)
        self.assertEqual(t.toList("preorder"), [83,64,59,73,71,95,84,88,97,96,99])
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 3)


    def test_leftRotationOnLargeTree(self):
        # TREE REPRESENTATION
        #
        #          _90_             ->              _97_
        #         /    \                           /    \
        #       83      97          ->           90      100
        #      /  \    /  \                     /  \    /   \
        #     64  84  96  100       ->        83    96  99   101
        #            /   /  \                /  \   /    /
        #          95  99    101    ->      64  84  95  98
        #             /                  
        #            98             -> 
        t = self.tree
        t.insert(90)
        t.insert(83)
        t.insert(97)
        t.insert(64)
        t.insert(84)
        t.insert(96)
        t.insert(100)
        t.insert(95)
        t.insert(99)
        t.insert(101)
        t.insert(98)


        self.assertEqual(t.size, 11)
        self.assertEqual(t.toList("preorder"), [97,90,83,64,84,96,95,100,99,98,101])
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 3)


    def test_leftRightRotationOnLargeTree(self):
        # TREE REPRESENTATION
        #
        #         54            ->               49
        #        /  \                           /  \
        #      41    55         ->            41    54
        #     /  \     \                     / \    / \
        #    38  49     56      ->         38   46 52  55
        #   /   /  \                      /      \       \
        # 36   46  52           ->      36       47       56
        #       \
        #        47             ->
        t = self.tree
        t.insert(54)
        t.insert(41)
        t.insert(55)
        t.insert(38)
        t.insert(49)
        t.insert(56)
        t.insert(36)
        t.insert(46)
        t.insert(52)
        t.insert(47)

        self.assertEqual(t.size, 10)
        self.assertEqual(t.toList("preorder"), [49,41,38,36,46,47,54,52,55,56])
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 3)


    def test_rightLeftRotationOnLargeTree(self):
        # TREE REPRESENTATION
        #
        #   3           ->          4
        #  / \                     / \
        # 2   7         ->        3   7
        #    / \                 /   / \
        #   4   8       ->      2   6   8
        #    \
        #     6         ->
        t = self.tree
        t.insert(3)
        t.insert(2)
        t.insert(7)
        t.insert(4)
        t.insert(8)
        t.insert(6)

        self.assertEqual(t.size, 6)
        self.assertEqual(t.toList("preorder"), [4,3,2,7,6,8])
        self.assertTrue(t.isBalanced())
        self.assertEqual(t.height(), 2)

class TestHeap(unittest.TestCase):
    pass


class TestRB(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()