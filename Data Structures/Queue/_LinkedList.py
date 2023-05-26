# ==================================================================================================
#       NODE
# ==================================================================================================

class Node:
    """
    Node defines the data structure to store a single item along with the index and reference to
    the `next` node. If `next` is null, then this node is the last on the list.
    """

    def __init__(self, item=None, previous=None, next=None):
        """
        Intilaize node with provided parameters:
        :param `item`: inferred type - item to be stored on the node.
        :param `previous_node`: Node - reference to the previous node.
        """
        self.next = next
        self.previous = previous
        self.item = item

        if not(previous == None):
            previous.next = self

        if not(next == None):
            next.previous = self


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
    `buildFrom(list)` - Generates a linked list from a built-in list.\n
    `sort(order)` - Sorts the list in ascending order by default. Set `order="dec"` to order in decending order.\n
    `clone()` - Deep copies the entire list and return the copy.\n
    `sublist(start, end)` - Finds and returns a sublist from the `start` index to the `end` index.
    """

    # RELATED TESTS
    #   test_initializeList()
    #   test_initialListSizeIsZero()
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

    # RELATED TESTS
    #   test_buildListOfTenNumbers()
    #   test_buildListOfTenStrings()
    #   test_buildEmptyList()
    def buildFrom(self, l:list):
        """
        Builds a singly linked list from the given built-in list.
        """
        for i in range(len(l)):
            self.append(l[i])


    # RELATED TESTS
    #   test_AppendOne()
    #   test_AppendMany()
    #   test_alternateAppendAndPrepend()
    #   test_AppendPrependPopAndDrop()
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


    # RELATED TESTS
    #   test_prependOne()
    #   test_prependMany()
    #   test_alternateAppendAndPrepend()
    #   test_AppendPrependPopAndDrop()
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

    # RELATED TESTS
    #   test_popOne()
    #   test_popMany()
    #   test_popFromEmptyList()
    #   test_alternatePopAndDrop()
    #   test_AppendPrependPopAndDrop()
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
        else:
            raise EmptyListException()
        
        return pop

    
    # RELATED TESTS
    #   test_dropOne()
    #   test_dropMany()
    #   test_dropFromEmptyList()
    #   test_alternatePopAndDrop()
    #   test_AppendPrependPopAndDrop()
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
        else:
            raise EmptyListException()

        return drop

    
    # RELATED TESTS
    #   test_removeItemAtGivenIndex()
    #   test_removeNonExistentItemFromTheList()
    #   test_removeElementAtValidIndex()
    #   test_removeElmentAtInvalidIndex()
    def remove(self, item):
        """
        Remove and return the given element.
        """
        if (not(self.isEmpty())):
            this_node = self.__head
            remove = this_node.item

            while remove != item:
                this_node = this_node.next
                if this_node == None:
                    raise RuntimeError("Element does not exist within the list!")
                remove = this_node.item
                
            previous_node = this_node.previous
            next_node = this_node.next
            previous_node.next = next_node
            self.__size -= 1
        else:
            raise EmptyListException()
        
        return remove


    # RELATED TESTS
    #   test_getElementAtIndex()
    #   test_getElementAtNegativeIndex()
    #   test_getElementAtIndexEqualToSize()
    #   test_getElementAtIndexGreaterThanSize()
    #   test_removeElementAtValidIndex()
    #   test_removeElmentAtInvalidIndex()
    def getAt(self, index: int) -> Node:
        """
        Return element at provided index.
        """
        if index >= 0 and index <= self.__size - 1:
            this_node = self.__head

            for i in range(index):
                this_node = this_node.next

            return this_node.item
        else:
            raise IndexError("Index out of bounds!")


    # RELATED TESTS
    #   test_popFromEmptyList()
    #   test_dropFromEmtyList()
    #   __listSate()
    def size(self):
        """
        Return the size of the list.
        """
        return self.__size
    

    # RELATED TESTS
    #   test_initialListSizeIsZero()
    #   test_appendOne()
    #   test_appendMany()
    #   test_appendStrings()
    #   test_prependOne()
    #   test_prependMany()
    #   test_popOne()
    #   test_popMany()
    def head(self):
        """
        Return the head element of the list.
        """
        if self.__head == None:
            return None

        return self.__head.item
    

    # RELATED TESTS
    #   test_initialListSizeIsZero()
    #   test_appendOne()
    #   test_appendMany()
    #   test_appendStrings()
    #   test_prependOne()
    #   test_prependMany()
    #   test_dropOne()
    #   test_dropMany()
    def tail(self):
        """
        Return the tail element of the list.
        """
        if self.__tail == None:
            return None

        return self.__tail.item
    

    # RELATED TESTS
    #   test_unpopulatedListIsEmpty()
    #   test_populatedListIsNotEmpty()
    def isEmpty(self) -> bool:
        """
        Check if the list is empty. Return `True` if it is.
        """
        return self.__size == 0
    

    # RELATED TESTS:
    #   test_CompareTheSameLists()
    #   test_CompareDifferentLists()
    #   test_CompareListsOfDifferentSizes()
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
    

    # --- SORT ---------------------------------------------------------------------------------------------------------------
    
    # RELATED TESTS
    #   test_sortAscending()
    #   test_sortDecending()
    #   test_sortEmptyList()
    #   test_sortSortedList()
    #   test_sortInvalidOrder()
    def sort(self, order="asc"):
        """
        Sort the linked list using quick-sort algorithm. `sort()` will arrange list elements in ascending order by default, unless otherwise stated by `order="dec"`.\n
        For a list of strings, all strings will be arranged by their sizes.
        """
        if order == "asc" or order == "dec":
            self.__quickSort(order)
        else:
            raise ValueError("Illegal sort order!")


    def __quickSort(self, order: str):
        # print("__quickSort()")
        head = self.__head
        tail = self.__tail
        self.__quickSortRec(head, tail, order)
        

    def __quickSortRec(self, low: Node, high: Node, order: str):
        # print("__quickSortRec()")

        if high != None and low != high and low != high.next:
            pivot = self.__partition(low, high, order)
            self.__quickSortRec(low, pivot.previous, order)
            self.__quickSortRec(pivot.next, high, order)


    def __partition(self, low: Node, high: Node, order: str) -> Node:
        # print("__partition()")

        # set pivot to the last element
        last = len(high.item) if type(high.item) == str else high.item

        # set i to the previous node of low (similar to i = -1)
        i = low.previous

        j = low

        while (j != high):
            j_item = len(j.item) if type(j.item) == str else j.item

            if (j_item <= last and order == "asc") or (j_item >= last and order == "dec"):

                i = low if i == None else i.next

                temp = i.item
                i.item = j.item
                j.item = temp

            j = j.next
            

        i = low if i == None else i.next
        
        temp = i.item
        i.item = j.item
        j.item = temp
        
        return i
    
    # --- SORT ---------------------------------------------------------------------------------------------------------------

    # RELATED TESTS
    #   test_cloneUpopulatedList()
    #   test_clonePrepopulatedList()
    def clone(self):
        """
        Return a deep-copied head of the linked list.
        """
        # Best case runtime - constant for when head is None
        # Worst case runtinme - linear for any list size
        head = self.__head

        nl = LinkedList()   # new list
        node = head

        while node != None:
            nl.append(node.item)
            node = node.next

        return nl
    

    # Related Tests
    #   test_getValidSublist()
    #   test_getSublistFromNegativeToValidIndex()
    #   test_getSublistFromValidToOutOfRangeIndex()
    #   test_getSublistOfEmptyList()
    #   test_getSublistOfAnotherSublist()
    def sublist(self, start:int, end:int):
        """
        Generate and return a sublist of the instance starting from the `start` index, finishing at `end` index.
        """
        if start == 0 and end == 0 and self.__size == 0:
            return LinkedList()
        if start < 0:
            raise IndexError("Start index is below zero!")
        if end >= self.__size:
            raise IndexError("End index is out of list range!")


        head = self.__head

        if head != None:
            ll = LinkedList()
            node = head

            for i in range(self.__size):
                if i >= start and i <= end:
                    ll.append(node.item)

                node = node.next

        else:
            raise EmptyListException("Cannot get the sublist of an empty list!")
        
        return ll



# ==================================================================================================
#       Exceptions
# ==================================================================================================

class EmptyListException(Exception):
    """
    Raised when the list is found empty.
    """
    def __init__(self, message="This list is empty.") -> None:
        self.message = message
        super().__init__(self.message)

    pass