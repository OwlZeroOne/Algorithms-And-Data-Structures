from _LinkedList import LinkedList

class Stack:
    
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
        Return `True` if the stack is empty. Otherwise, return `False`.
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