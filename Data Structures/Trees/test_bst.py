import unittest
from bst import *

class TestBst(unittest.TestCase):
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
    # The tree is implied by `insertTen()`.


    def setUp(self) -> None:
        self.bst = BinarySearchTree()


    def test_initialState(self):
        """
        Test the initial state of the binary search tree. Expected size should be 0.
        """
        bst = self.bst

        self.assertEqual(bst.size(), 0)
        self.assertEqual(bst.toString("inorder"), "[]")
        self.assertEqual(bst.toString("preorder"), "[]")
        self.assertEqual(bst.toString("postorder"), "[]")


    def test_insertOne(self):
        """
        Insert one item into the BST. Tree should have the final size of 1 and should output `[x]` for every ordering.
        """
        bst = self.bst
        bst.insert(47)

        self.assertEqual(bst.size(), 1)
        self.assertEqual(bst.toString("inorder"), "[47]")
        self.assertEqual(bst.toString("preorder"), "[47]")
        self.assertEqual(bst.toString("postorder"), "[47]")

        
    def test_insertThree(self):
        """
        Insert three items into the tree where one item is smaller than the root and the other is greater. Final size should be 3 and output should comply with the ordering system.
        """
        # Resulting tree should be
        #
        #           47
        #          /  \
        #        12    54
        #
        bst = self.bst
        bst.insert(47)
        bst.insert(12)
        bst.insert(54)

        self.assertEqual(bst.size(), 3)
        self.assertEqual(bst.toString("inorder"), "[12,47,54]")
        self.assertEqual(bst.toString("preorder"), "[47,12,54]")
        self.assertEqual(bst.toString("postorder"), "[12,54,47]")


    def insertTen(input:BinarySearchTree):
        bst = input
        bst.insert(47)
        bst.insert(12)
        bst.insert(54)
        bst.insert(10)
        bst.insert(33)
        bst.insert(42)
        bst.insert(89)
        bst.insert(76)
        bst.insert(90)
        bst.insert(24)
        return bst


    def test_insertTen(self):
        """
        Insert ten random items into the tree. Output should be of size 10 and should comply with the ordering system.
        """
        bst = TestBst.insertTen(self.bst)

        self.assertEqual(bst.size(), 10)
        self.assertEqual(bst.toString("inorder"), "[10,12,24,33,42,47,54,76,89,90]")
        self.assertEqual(bst.toString("preorder"), "[47,12,10,33,24,42,54,89,76,90]")
        self.assertEqual(bst.toString("postorder"), "[10,24,42,33,12,76,90,89,54,47]")


    def test_deleteExistingLeafNode(self):
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
        bst = TestBst.insertTen(self.bst)
        bst.delete(42)

        self.assertEqual(bst.size(), 9)
        self.assertEqual(bst.toString("inorder"), "[10,12,24,33,47,54,76,89,90]")
        self.assertEqual(bst.toString("preorder"), "[47,12,10,33,24,54,89,76,90]")
        self.assertEqual(bst.toString("postorder"), "[10,24,33,12,76,90,89,54,47]")


    def test_deleteExistingNodeWithOneChild(self):
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
        bst = TestBst.insertTen(self.bst)
        bst.delete(54)

        self.assertEqual(bst.size(), 9)
        self.assertEqual(bst.toString("inorder"), "[10,12,24,33,42,47,76,89,90]")
        self.assertEqual(bst.toString("preorder"), "[47,12,10,33,24,42,89,76,90]")
        self.assertEqual(bst.toString("postorder"), "[10,24,42,33,12,76,90,89,47]")


    def test_deleteExistingNodeWithTwoChildren(self):
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
        bst = TestBst.insertTen(self.bst)
        bst.delete(12)

        self.assertEqual(bst.size(), 9)
        self.assertEqual(bst.toString("inorder"), "[10,24,33,42,47,54,76,89,90]")
        self.assertEqual(bst.toString("preorder"), "[47,24,10,33,42,54,89,76,90]")
        self.assertEqual(bst.toString("postorder"), "[10,42,33,24,76,90,89,54,47]")

        bst2 = BinarySearchTree()
        bst2 = TestBst.insertTen(bst2)
        bst2.delete(47)

        self.assertEqual(bst2.size(), 9)
        self.assertEqual(bst2.toString("inorder"), "[10,12,24,33,42,54,76,89,90]")
        self.assertEqual(bst2.toString("preorder"), "[54,12,10,33,24,42,89,76,90]")
        self.assertEqual(bst2.toString("postorder"), "[10,24,42,33,12,76,90,89,54]")


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
        bst = TestBst.insertTen(self.bst)
        bst.delete(12)
        bst.delete(33)
        bst.delete(89)
        bst.delete(47)
        # Final state:
        #
        #           54
        #          /  \
        #        24    90
        #       /  |   |
        #     10   42  76
        #                 
        self.assertEqual(bst.size(), 6)
        self.assertEqual(bst.toString("inorder"), "[10,24,42,54,76,90]")
        self.assertEqual(bst.toString("preorder"), "[54,24,10,42,90,76]")
        self.assertEqual(bst.toString("postorder"), "[10,42,24,76,90,54]")


    def test_deleteNonExistentNode(self):
        """
        Attempt to remove a non-existent node from a populated tree. Should raise a `RuntimeError` exception.
        """
        bst = TestBst.insertTen(self.bst)
        with self.assertRaises(RuntimeError):
            bst.delete(4)


    def test_validLookup(self):
        """
        Search for a node that exists within the list. Test on four different cases that exist within the tree.
        """
        t1 = 33
        t2 = 76
        t3 = 47
        t4 = 10

        bst = TestBst.insertTen(self.bst)
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
        bst = TestBst.insertTen(self.bst)
        
        with self.assertRaises(RuntimeError):
            bst.lookup(t)


    def test_findMaximum(self):
        """
        Find and return the node with the greatest key.
        """
        bst = TestBst.insertTen(self.bst)
        max = bst.maximum()

        self.assertEqual(max.key, 90)


    def test_findMinimum(self):
        """
        Find and return the node with the smallest key.
        """
        bst = TestBst.insertTen(self.bst)
        min = bst.minimum()

        self.assertEqual(min.key, 10)


    def test_deleteNodeFromAnEmptyTree(self):
        """
        Attempt to remove a node from an empty tree. A `RuntimeError` exception should be thrown.
        """
        with self.assertRaises(RuntimeError):
            self.bst.delete(45)

    


if __name__ == "__main__":
    unittest.main()