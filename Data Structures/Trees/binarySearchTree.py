from binaryTree import BinaryTree
from nodes import BinaryNode

class BinarySearchTree(BinaryTree):
    """
    A Binary Search Tree (BST) is a binary tree that satisfies the following properties:
    - Left children contain keys lesser than parents'.
    - Right children contain keys greater than parents'.
    - Every subtree is also a BST.
    """
    
    N = BinaryNode
    # RELATED TESTS
    #   TestBinarySearchTree.test_initialState()
    def __init__(self, maxSize):
        super().__init__(maxSize)
        

    # RELATED TESTS
    #   TestBinarySearchTree.setUp()
    def insert(self, key) -> BinaryNode:
        
        if self.root == None:
            newChild = BinaryNode(key, None)
            self.root = newChild
        else:
            newChild = self.__insert(self.root, key)

        self.size += 1
        return newChild


    def __insert(self, parnet:N, key) -> BinaryNode:

        newChild = BinaryNode(key, parnet)

        if parnet.key == key:
            raise ValueError("Key already present...")
        
        elif key < parnet.key:
            if parnet.left == None:
                parnet.left = newChild
            else:
                 return self.__insert(parnet.left, key)
        else:
            if parnet.right == None:
                parnet.right = newChild
            else:
                return self.__insert(parnet.right, key)

        return newChild


    # RELATED TESTS
    #   test_deleteExistingLeafNode()
    #   test_deleteExistingNodeWithOneChild()
    #   test_deleteExistingNodeWithTwoChildren()
    #   test_deleteMany()
    #   test_deleteNonExistentNode()
    #   test_deleteNodeFromAnEmptyTree()
    def delete(self, key):

        if not(self.isEmpty()):
            target:BinaryNode = self.lookup(key)
            parent:BinaryNode = target.parent
            
            # Target has no children
            if target.left == None and target.right == None:
                self.__deleteWithNoChildren(target, parent)
            
            # Target has two children
            elif target.left != None and target.right != None:
                self.__deleteWithTwoChildren(target, parent)

            # Target has one child
            else:
                self.__deleteWithOneChild(target, parent)
                
        else:
            raise RuntimeError("Tree is empty!")

        self.size -= 1
            

    def __deleteWithNoChildren(self, target:N, parent:N):

        if parent.left == target:
            parent.left = None

        elif parent.right == target:
            parent.right = None

        else:
            raise RuntimeError("Unexpected error!")
            

    def __deleteWithOneChild(self, target:N, parent:N):
        
        child = target.left if target.left != None else target.right

        if parent.left == target:
            parent.left = child

        elif parent.right == target:
            parent.right = child

        else:
            raise RuntimeError("Unexpected error!")


    def __deleteWithTwoChildren(self, target:N, parent:N):
        ldor = self.__leftmostDecendentOf(target.right)
        ldor_parent = ldor.parent
        target.key = ldor.key

        # ldor has no children
        if ldor.left == None and ldor.right == None:
            self.__deleteWithNoChildren(ldor, ldor_parent)
        
        # ldor has one child
        elif self._XOR(ldor.left != None, ldor.right != None):
            self.__deleteWithOneChild(ldor, ldor_parent)


    def __leftmostDecendentOf(self, node:N):
        
        if node.left != None:
            return self.__leftmostDecendentOf(node.left)
        else:
            return node

    # RELATED TESTS
    #   test_validLookup()
    #   test_invalidLookup()
    def lookup(self, key) -> N:
        return self.__lookup(self.root, key)


    def __lookup(self, node: N, find) -> bool:
        
        if node == None:
            raise RuntimeError("Could not find element...")
        
        elif node.key == find:
            return node
        
        elif find < node.key:
            return self.__lookup(node.left, find)
        
        else: # if find > node.key
            return self.__lookup(node.right, find)
        
    # RELATED TESTS
    #   test_findMaximum()
    def maximum(self) -> N:
        """
        Return the maximum key in the tree.
        """
        return self.__max(self.root)
    

    def __max(self, node:N) -> N:
        
        if node.right != None:
            return self.__max(node.right)
        else:
            return node
        

    # RELATED TESTS
    #   test_findMinimum()
    def minimum(self) -> N:
        """
        Return the minimum key in the tree.
        """
        return self.__min(self.root)
    

    def __min(self, node:N) -> N:
        
        if node.left != None:
            return self.__min(node.left)
        else:
            return node
    

    def isEmpty(self) -> bool:
        return self.size == 0
    

    def _XOR(self, a, b) -> bool:
        return (a and not(b)) or (b and not(a))
