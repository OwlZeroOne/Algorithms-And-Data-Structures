class Node:

    def __init__(self, parent, key):
        self.parent = parent
        self.key = key
        self.left = self.right = None


class BinarySearchTree:
    """
    The binary search tree is a non-balanced binary tree that is organized in such a way that the left children of each node have smaller values than the node, while right children have greate values. The current implementation supports;\n
    `insert(key)` - insert `key` into the tree with respect to the binary-search-try property.\n
    `search(key)` - perform a traversal on the tree to find the given `key`.\n
    `delete(key)` - remove given `key` from the tree by performing a search traversal and node rearrangement.\n
    `minimum()` - return the minumum value of the tree.\n
    `maximum()` - return the maximum value of the tree.\n
    `treeWalk(order)` - print the tree using the `inorder`, `preorder` or `postorder` setting.
    """

    # RELATED TESTS
    #   test_initialState()
    def __init__(self):
        self.root = None
        self._size = 0


    # RELATED TESTS
    #   test_insertOne()
    #   test_insertThree()
    #   test_insertTen()
    def insert(self, key) -> None:
        
        if self.root == None:
            self.root = Node(None, key)
        else:
            self.__newNode(self.root, key)

        self._size += 1


    def __newNode(self, node: Node, key):

        if node.key == key:
            raise ValueError("Key already present...")
        
        elif key < node.key:
            if node.left == None:
                node.left = Node(node, key)
            else:
                self.__newNode(node.left, key)
        else:
            if node.right == None:
                node.right = Node(node, key)
            else:
                self.__newNode(node.right, key)


    # RELATED TESTS
    #   test_deleteExistingLeafNode()
    #   test_deleteExistingNodeWithOneChild()
    #   test_deleteExistingNodeWithTwoChildren()
    #   test_deleteMany()
    #   test_deleteNonExistentNode()
    #   test_deleteNodeFromAnEmptyTree()
    def delete(self, j):

        if not(self.isEmpty()):
            target:Node = self.lookup(j)
            parent:Node = target.parent
            
            # Target has no children
            if target.left == None and target.right == None:
                self.__deleteWithNoChildren(target, parent)
            
            # Target has one child
            elif self._XOR(target.left != None, target.right != None):
                self.__deleteWithOneChild(target, parent)
                
            # Target has two children
            else:
                self.__deleteWithTwoChildren(target, parent)
        else:
            raise RuntimeError("Tree is empty!")

        self._size -= 1
            

    def __deleteWithNoChildren(self, target:Node, parent:Node):

        if parent.left == target:
            parent.left = None

        elif parent.right == target:
            parent.right = None

        else:
            raise RuntimeError("Unexpected error!")
            

    def __deleteWithOneChild(self, target:Node, parent:Node):
        
        child = target.left if target.left != None else target.right

        if parent.left == target:
            parent.left = child

        elif parent.right == target:
            parent.right = child

        else:
            raise RuntimeError("Unexpected error!")


    def __deleteWithTwoChildren(self, target:Node, parent:Node):
        ldor = self.__leftmostDecendentOf(target.right)
        ldor_parent = ldor.parent
        target.key = ldor.key

        # ldor has no children
        if ldor.left == None and ldor.right == None:
            self.__deleteWithNoChildren(ldor, ldor_parent)
        
        # ldor has one child
        elif self._XOR(ldor.left != None, ldor.right != None):
            self.__deleteWithOneChild(ldor, ldor_parent)


    def __leftmostDecendentOf(self, node:Node):
        
        if node.left != None:
            return self.__leftmostDecendentOf(node.left)
        else:
            return node

    # RELATED TESTS
    #   test_validLookup()
    #   test_invalidLookup()
    def lookup(self, key) -> Node:
        return self.__lookup(self.root, key)


    def __lookup(self, node: Node, find) -> bool:
        
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
    def maximum(self) -> Node:
        """
        Return the maximum key in the tree.
        """
        return self.__max(self.root)
    

    def __max(self, node:Node) -> Node:
        
        if node.right != None:
            return self.__max(node.right)
        else:
            return node
        

    # RELATED TESTS
    #   test_findMinimum()
    def minimum(self) -> Node:
        """
        Return the minimum key in the tree.
        """
        return self.__min(self.root)
    

    def __min(self, node:Node) -> Node:
        
        if node.left != None:
            return self.__min(node.left)
        else:
            return node
        

    # RELATED TESTS
    #   test_initialState()
    #   test_insertOne()
    #   test_insertThree()
    #   test_insertTen()
    def toString(self, order="inorder") -> str:
        """
        Print tree keys in one of the following orders:\n
        `"inorder"` - print root nodes between left and right subtrees (default).\n
        `"preorder"` - print root nodes before left and right subtrees.\n
        `"postorder"` - print root nodes after left and right subtrees.
        """
        if self.root != None:
            if order == "inorder":
                return "["+self.__inorderTreeWalk(self.root)+"]"

            elif order == "preorder":
                return "["+self.__preorderTreeWalk(self.root)+"]"

            elif order == "postorder":
                return "["+self.__postorderTreeWalk(self.root)+"]"

            else:
                raise ValueError("Unexpected order parameter!")
        else:
            return "[]"
        

    def toList(self, order="inorder"):
        """
        Convert the tree to a list in provided order:\n
        `"inorder"` - root nodes between left and right subtrees (default).\n
        `"preorder"` - root nodes before left and right subtrees.\n
        `"postorder"` - root nodes after left and right subtrees.
        """
        pass
        
    # TODO Have treewalks return a list to toList(). If print required, send to toString().
    
    def __inorderTreeWalk(self, node:Node):
        """
        Print tree keys with root nodes being printed between left and right child nodes/subtrees.
        """
        if node != None:
            return str.format("{}{}{}",
                              self.__inorderTreeWalk(node.left) + "," if node.left != None else "",
                              node.key,
                              ("," if node.right != None else "") + self.__inorderTreeWalk(node.right))
        else:
            return ""
            


    def __preorderTreeWalk(self, node:Node):
        """
        Print tree keys with root nodes being printed before left and right child nodes/subtrees.
        """
        if node != None:
            return str.format("{}{}{}",
                              node.key,
                              ("," if node.left != None else "") + self.__preorderTreeWalk(node.left),
                              ("," if node.right != None else "") + self.__preorderTreeWalk(node.right))
        else:
            return ""


    def __postorderTreeWalk(self, node:Node):
        """
        Print tree keys with root nodes being printed after left and right child nodes/subtrees.
        """
        if node != None:
            return str.format("{}{}{}",
                              self.__postorderTreeWalk(node.left) + "," if node.left != None else "",
                              self.__postorderTreeWalk(node.right) + "," if node.right != None else "",
                              node.key)
        else:
            return ""


    def size(self):
        return self._size
    

    def isEmpty(self) -> bool:
        return self._size == 0
    

    def _XOR(self, a, b) -> bool:
        return (a and not(b)) or (b and not(a))
