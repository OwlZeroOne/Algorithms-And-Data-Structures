from nodes import BinaryNode
from treeInterface import TreeInterface
from _myQueue import Queue

class BinaryTree(TreeInterface):

    N = BinaryNode

    # RELATED TESTS
    #   test_initialize()
    def __init__(self, maxSize) -> None:
        self.root:BinaryNode = None
        self.maxSize = maxSize
        self.size = 0


    # RELATED TESTS
    #   TestBinaryTree.test_insertOne()
    #   TestBinaryTree.test_insertToParentWithNoRoot()
    #   TestBinaryTree.test_insertThree()
    #   TestBinaryTree.test_insertToNonExistentParent()
    #   TestBinaryTree.test_insertToParentWithTwoChildren()
    #   TestBinaryTree.test_insertExistingKey()
    #   TestBinaryTree.test_insertToFullTree()
    #   TestBinaryTree.test_differentFullTrees()
    def insert(self, key, parentKey=None) -> BinaryNode:
        """
        Insert a new `key` to a parent node of `parentKey` if it does not yet exist within the tree. Keys are added from left to right for each parent node. If the parent already has two children, a `ValueError` is raised.
        """

        # Only insert if key doesn't yet exist.
        if self.lookup(key) == None:

            # Check if tree is full or not.
            if self.size < self.maxSize:

                newChild = BinaryNode(key, None)

                # Ensure that parent key is `None` if there is no root node.
                if self.root == None:
                    if parentKey != None:
                        raise ValueError("Root has no parents!")
                    
                    self.root = newChild
                    self.size += 1
                else:
                    # Ensure that parent key is present.
                    if parentKey == None:
                        raise ValueError("Parent key must be provided for trees with more than one node!")
                        
                    parent:BinaryNode = self.lookup(parentKey)
                    newChild.parent = parent

                    # Check whether parent exists.
                    if parent != None:
                        if parent.left == None:
                            parent.left = newChild
                            self.size += 1

                        elif parent.right == None:
                            parent.right = newChild
                            self.size += 1

                        else:
                            raise ValueError("This parent already has two children!")
                    else:
                        raise LookupError("This parent does not exist!")
            else:
                raise OverflowError("The binary tree is full!")    
        else:
            raise LookupError("Node with this key already exists!")
        
        return newChild
    

    def isBalanced(self) -> bool:
        """
        Check if the tree is balanced using the balanced factor `bf`. A tree is balanced when -1 <= `bf` <= 1.
        """
        bf = self._balanceFactor(self.root)
        return bf >= -1 and bf <= 1
        

    def _balanceFactor(self, node:N):
        
        if node != None:
            left:BinaryNode = node.left
            right:BinaryNode = node.right

            lh = rh = 0

            if left != None:
                lh = self.heightOfNode(left) + 1

            if right != None:
                rh = self.heightOfNode(right) + 1

            return lh - rh
        else:
            return 0
    

    def heightOfKey(self, key) -> int: 
        """
        Evaluate the height of a `node` given a particular `key`.
        """
        target:BinaryNode = self.lookup(key)
        if target == None:
            raise LookupError("Node with given key not found!")

        return self.heightOfNode(target)
    

    # RELATED TESTS
    #   test_heightOfNode()
    def heightOfNode(self, target:N) -> int:
        """
        Calculate the height of the `target` node provided.
        """
        return self.__height(target)
        

    # RELATED TESTS
    #   test_heightOfEmptyTree()
    #   test_treeHeight()
    def height(self) -> int:
        """
        Recursively evaluate the height of the tree by taking the maximum height of each subtree.
        """
        if not(self.isEmpty()):
            # Execute recursive function.
            return self.__height(self.root)
        else:
            return 0


    def __height(self, src:N, counter=-1):

        if src != None:
            counter += 1
            return max(
                self.__height(src.left, counter),
                self.__height(src.right, counter))
        else:
            return counter
    
    
    # RELATED TESTS
    #   TestBinaryTree.test_deleteOneLeaf()
    #   TestBinaryTree.test_deleteOneChildParent()
    #   TestBinaryTree.test_deleteTwoChildParent()
    #   TestBinaryTree.test_deleteNonExistentKey()
    def delete(self, key) -> N:
        """
        - If `key` has no children, just delete reference from parent.\n
        - If `key` has two children, relpace the key with its right child.\n
        - If `key` has one (left) child, replace the key with it.
        """

        # Only run if the tree is not empty.
        if not(self.isEmpty()):

            # Check if given key exists.
            target = self.lookup(key)
            if target != None:
                self.__delete(target)
                self.size -= 1
            else:
                raise LookupError("Given key does not exist!")
        else:
            raise LookupError("Cannot delete from empty tree!")
        

    def __delete(self, target:N):
        if target.left == None and target.right == None:
            parent:BinaryNode = target.parent
            if parent.left == target:
                parent.left = None
            else:
                parent.right = None

        elif target.left != None and target.right != None:
            next:BinaryNode = target.right
            last:BinaryNode = next

            while last.right != None:
                last = last.right

            target.key = last.key
            self.__delete(last)
        
        else:
            next:BinaryNode = target.left

            target.key = next.key
            target.left = next.left
            target.right = next.right
    

    def lookup(self, targetKey) -> N:
        """
        Search for the parent using Breadth-First-Search. Return node once found, else return `None`.
        """
        if not(self.isEmpty()):
            q = Queue()
            q.enqueue(self.root)

            while not(q.isEmpty()):
                current:BinaryNode = q.dequeue()

                if current.key == targetKey:
                    return current

                if current.left != None:
                    q.enqueue(current.left)

                if current.right != None:
                    q.enqueue(current.right)

        return None
    

    # RELATED TESTS
    #   test_depthOfNode()
    def depthOf(self, key) -> int:
        """
        Find and return the depth of the node by counting down its ancestors until the root is reached.
        """
        target:BinaryNode = self.lookup(key)
        if target != None:
            counter = 0
            parent:BinaryNode = target.parent
            while parent != None:
                parent = parent.parent
                counter += 1

            return counter

        else:
            raise LookupError("Key node not found!")
    

    def isEmpty(self) -> bool:
        """
        Check whether the tree is empty by checking if the size is zero.
        """
        return self.size <= 0
    

    def toList(self, order="inorder") -> list:
        """
        Convert the tree into a list using either `"inorder"`, `"preorder"` or `"postorder"` tree walk algorithms.
        """
        if order=="inorder":
            return self._inorderWalk(self.root)
        
        elif order=="preorder":
            return self._preorderWalk(self.root)
        
        elif order=="postorder":
            return self._postorderWalk(self.root)
        
        else:
            raise ValueError("Invalid argument for list order!")
    

    def _inorderWalk(self, node:N) -> list:
        """
        Order tree elements from left to right and return as a list.
        """
        if node != None:
            left = self._inorderWalk(node.left)
            mid = [node.key]
            right = self._inorderWalk(node.right)

            return left + mid + right
        else:
            return []
        

    def _preorderWalk(self, node:N) -> list:
        """
        Order tree elements such that roots of each subtree have presedence over their descendants.
        """
        if node != None:
            left = [node.key]
            mid = self._preorderWalk(node.left)
            right = self._preorderWalk(node.right)

            return left + mid + right
        else:
            return []
        

    def _postorderWalk(self, node:N) -> list:
        """
        Order tree elements such that descendants have presedence over their subtree roots.
        """
        if node != None:
            left = self._postorderWalk(node.left)
            mid = self._postorderWalk(node.right)
            right = [node.key]

            return left + mid + right
        else:
            return []