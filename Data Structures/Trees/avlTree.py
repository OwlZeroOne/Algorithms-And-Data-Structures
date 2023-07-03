from binarySearchTree import BinarySearchTree as bst
from nodes import BinaryNode
from _myStack import Stack


class AvlTree(bst):
    """
    A self-balancing Binary Search Tree (BST), where the difference between heights of nodes of left and right subtrees cannot be more than one. It is based on the balance factor, whihc is calculated by the height of the right subtree minus the heigfht of the left subtree.
    """
    N = BinaryNode

    def __init__(self, maxSize):
        super().__init__(maxSize)


    def insert(self, key) -> BinaryNode:
        """
        Insert new node into the binary tree, followed by possible rotations of root's children.
        - Perform right rotation on the left subtree if `balanceFactor` > 1.
        - Perform left rotation on the right subtree if `balanceFactor` < -1.
        """
        node:BinaryNode = super().insert(key)
        stack = Stack()

        while node != None:
            bf = abs(self._balanceFactor(node))
            # print(node.key, self._balanceFactor(node))
            if bf > 1:
                parent = node
                child = stack.drop()
                grandChild = stack.drop()
                # print(parent, child, grandChild)
                self._rotate(parent, child, grandChild)
                # print(self.root.key)
                break
            stack.append(node)
            node = node.parent

    

    def delete(self, key):
        return super().delete(key)
    

    def lookup(self, key) -> N:
        return super().lookup(key)
    

    def _balance(self):
        pass
    

    def _rotate(self, parent:N, child:N, grandChild:N):
        
        if child == parent.left:
            if grandChild == child.left:
                # print("Rotate right")
                self._rotateRight(parent, child)

            elif grandChild == child.right:
                # print("Rotate left-right")
                self._rotateLeftRight(parent, child, grandChild)

            else:
                raise RuntimeError("Illegal child node!")

        elif child == parent.right:
            if grandChild == child.right:
                # print("Rotate left")
                self._rotateLeft(parent, child)

            elif grandChild == child.left:
                # print("Rotate right-left")
                self._rotateRightLeft(parent, child, grandChild)

            else:
                raise RuntimeError("Illegal child node!")
        else:
            raise RuntimeError("Illegal child node!")
    

    def _rotateLeft(self, parent:N, child:N):
        
        if parent == self.root:
            self.root = child

        leftGrandChild = child.left
        parent.right = leftGrandChild

        child.left = parent


    def _rotateRight(self, parent:N, child:N):

        if parent == self.root:
            self.root = child

        rightGrandChild = child.right
        parent.left = rightGrandChild

        child.right = parent

    
    def _rotateLeftRight(self, parent:N, child:N, grandChild:N):

        self._rotateLeft(child, grandChild)
        self._rotateRight(parent, grandChild)


    def _rotateRightLeft(self, parent:N, child:N, grandChild:N):

        self._rotateRight(child, grandChild)
        self._rotateLeft(parent, grandChild)

