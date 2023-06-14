from _LinkedList import LinkedList

class Queue:
    """
    Queue data structure that uses the doubly-linked list implementation. Current implementation of the queue provides the following:\n
    `enqueue(item)` - Append a new element to the queue.\n
    `dequeue()` - Pop the head of the queue.\n
    `peek()` - Return the head of the queue without removing it.\n
    `isEmpty()` - Check if the queue is empty.\n
    `size()` - Return current size of the queue.\n
    `toLinkedList()` - Return the linked list version of the queue.
    """
    def __init__(self):
        """
        Intialize the queue by creating a new linked list instance.
        """
        self.__list = LinkedList()


    def __str__(self) -> str:
        return self.__list.__str__()


    def enqueue(self, item):
        self.__list.append(item)
        pass


    def dequeue(self):
        """
        Pop and return the queue of the list.
        """
        return self.__list.pop()


    def peek(self):
        """
        Return the head of the queue without removing it.
        """
        return self.__list.head()


    def isEmpty(self):
        """
        Return `True` if the queue is empty. Otherwise, return `False`.
        """
        return self.__list.isEmpty()
    

    def size(self):
        """
        Return the size of the queue.
        """
        return self.__list.size()
    

    def toLinkedList(self) -> LinkedList:
        """
        Return the linked list of the queue.
        """
        return self.__list