from _LinkedList import LinkedList

class Stack:
    """
    Stack data structure that uses the doubly-linked list implementation. Current implementation of the stack provides the following:\n
    `append(item)` - Append a new element to the stack.\n
    `drop()` - Drop the tail of the stack.\n
    `peek()` - Return the tail of the stack without removing it.\n
    `isEmpty()` - Check if the stack is empty.\n
    `size()` - Return current size of the stack.\n
    `toLinkedList()` - Return the linked list version of the stack.
    """

    # RELATED TESTS
    #   test_initializeStack()
    def __init__(self) -> None:
        """
        Initialize the stack by creating a new linked list instance.
        """
        self.__list = LinkedList()


    def __str__(self) -> str:
        return self.__list.__str__()


    # RELATED TESTS
    #   test_appendOne()
    #   test_appendMany()
    #   test_appendAndDrop()
    def append(self, item):
        """
        Add new `item` onto the stack.
        """
        self.__list.append(item)


    # RELATED TESTS
    #   test_dropOne()
    #   test_dropMany()
    #   test_dropFromAnEmptyList()
    #   test_appendAndDrop()
    def drop(self):
        """
        Remove and return the tail from the stack.
        """
        return self.__list.drop()


    # RELATED TESTS
    #   test_peekPopulatedStack()
    #   test_peekEmptyStack()
    def peek(self):
        """
        Return the tail of the stack without removing it.
        """
        return self.__list.tail()


    # RELATED TESTS
    #   test_populatedIsNotEmpty()
    #   test_unpopulatedIsEmpty()
    def isEmpty(self):
        """
        Return `True` if the stack is empty. Otherwise, return `False`.
        """
        return self.__list.isEmpty()
    

    def size(self):
        """
        Return the size of the stack.
        """
        return self.__list.size()
    

    # RELATED TESTS
    #   test_toLinkedList()
    def toLinkedList(self) -> LinkedList:
        """
        Return the linked list of the queue.
        """
        return self.__list