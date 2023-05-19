# ==================================================================================================
#       NODE
# ==================================================================================================

class Node:
    """
    Node defines the data structure to store a single item along with the index and reference to
    the `next` node. If `next` is null, then this node is the last on the list.
    """

    def __init__(self, item, previous=None, next=None):
        """
        Intilaize node with provided parameters:
        :param `item`: inferred type - item to be stored on the node.
        :param `previous_node`: Node - reference to the previous node.
        """
        self.next = next
        self.previous = previous
        self.item = item


    def __str__(self) -> str:
        """
        Return the string representation of the node's element.
        """
        return str(self.item)
    

    def equals(self, other_node) -> bool:
        """
        Compare nodes by their elements
        """
        return self.item == other_node.item
        



# ==================================================================================================
#       LIST
# ==================================================================================================

class LinkedList:
    """
    Two-way (doubly) linked list consisting of an arbitrary amount of nodes, dependent on the number of elements stored. This version currently consists of the following operations:\n
    `append(item)` - Add a new element to the end of the list.\n
    `prepend(item)` - Add a new element to the start of the list.\n
    `pop()` - Removes and returns the head element from the list.\n
    `drop()` - Removes and returns the tail element from the list.\n
    `remove(item)` - Removes and returns specified item from the list.\n
    `getAt(index)` - Returns element at specified index.\n
    `size()` - Returns the size of the list.\n
    `head()` - Returns the head element of the list.\n
    `tail()` - Returns the tail element of the list.\n
    `isEmpty()` - Returns `True` if the list is empty. Otherwise `False`.\n
    `equals(other_list)` - Compares this list with `other_list` and returns `True` if they are identical (order-dependent).\n
    `buildFrom(list)` - Generates a linked list from a built-in list.
    """

    def __init__(self):
        """
        Initialize empty list with empty head and empty tail.
        """
        self.__size: int = 0
        self.__head: Node = None
        self.__tail: Node = None


    def __str__(self) -> str:
        """
        Return the string representation of the list, starting from its head.
        """
        output = ""

        if self.__head != None:
            this_node = self.__head
            # output = str.format("[{}]", self.__head.__str__() if self.__head != None else "")

            while this_node != None:
                output += str.format("{}{}",this_node.item,("," if this_node.next != None else ""))
                # print(this_node.next().get())
                this_node = this_node.next

        return str.format("[{}]", output)

    
    def buildFrom(self, l:list):
        """
        Builds a singly linked list from the given built-in list.
        """
        for i in range(len(l)):
            self.append(l[i])


    def append(self, item):
        """
        Add item to the end of the list.
        """
        new_node = Node(item)

        if self.__head == None:
            self.__head = self.__tail = Node(item)

        else:
            self.__tail.next = Node(item, self.__tail, None)
            self.__tail = self.__tail.next


        self.__size += 1


    def prepend(self, item):
        """
        Add item to the start of the list.
        """
        if self.__head == None:
            self.__head = self.__tail = Node(item)

        else:
            self.__head.previous = Node(item, None, self.__head)
            self.__head = self.__head.previous

        self.__size += 1


    def pop(self):
        """
        Remove and return the first element in the list.
        """
        if not(self.isEmpty()):
            pop = self.__head.item

            if (self.__head == self.__tail):
                self.__head = self.__tail = None
            else:
                self.__head = self.__head.next
                self.__head.previous = None
        
            self.__size -= 1

        return pop
    

    def drop(self):
        """
        Remove and return the last element in the list.
        """
        if not(self.isEmpty()):
            drop = self.__tail.item

            if (self.__head == self.__tail):
                self.__head = self.__tail = None
            else:
                self.__tail = self.__tail.previous
                self.__tail.next = None
        
            self.__size -= 1

        return drop

    
    def remove(self, item):
        """
        Remove and return the given element.
        """
        this_node = self.__head
        remove = this_node.item

        while remove != item:
            this_node = this_node.next
            remove = this_node.item
            if this_node == None:
                raise IndexError("List index is out of range!")
            
        previous_node = this_node.previous
        next_node = this_node.next
        previous_node.next = next_node
        self.__size -= 1
        
        return remove


    def getAt(self, index: int) -> Node:
        """
        Return element at provided index.
        """
        this_node = self.__head

        for i in range(index):
            this_node = this_node.next

        return this_node.item


    
    def size(self):
        """
        Return the size of the list.
        """
        return self.__size
    

    def head(self):
        """
        Return the head element of the list.
        """
        if self.__head == None:
            return None

        return self.__head.item
    

    def tail(self):
        """
        Return the tail element of the list.
        """
        if self.__tail == None:
            return None

        return self.__tail.item
    

    def isEmpty(self) -> bool:
        """
        Check if the list is empty. Return `True` if it is.
        """
        return self.__size == 0
    

    def equals(self, other_list) -> bool:
        """
        Compare linked list to another list
        """
        
        if self.__size == other_list.__size:
            this_node = self.__head
            other_node = other_list.__head

            for i in range(self.__size):
                if not(this_node.equals(other_node)):
                    return False
                
                this_node = this_node.next
                other_node = other_node.next
            
            return True
        
        return False
