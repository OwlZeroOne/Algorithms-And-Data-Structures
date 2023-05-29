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

    def __init__(self) -> None:
        """
        Initialize the stack by creating a new linked list instance.
        """
        self.__list = LinkedList()


    def __str__(self) -> str:
        return self.__list.__str__()


    def append(self, item):
        """
        Add new `item` onto the stack.
        """
        self.__list.append(item)


    def drop(self):
        """
        Remove and return the tail from the stack.
        """
        return self.__list.drop()


    def peek(self):
        """
        Return the tail of the stack without removing it.
        """
        return self.__list.tail()


    def isEmpty(self):
        """
        Return `True` if the queue is empty. Otherwise, return `False`.
        """
        return self.__list.isEmpty()
    

    def size(self):
        """
        Return the size of the stack.
        """
        return self.__list.size()
    

    def toLinkedList(self) -> LinkedList:
        """
        Return the linked list of the queue.
        """
        return self.__list