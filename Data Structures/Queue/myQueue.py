from _LinkedList import LinkedList

class Queue:
    """
    Queue data structure that uses the doubly-linked list implementation. Current implementation of the queue provides the following:\n
    `enqueue(item)` - Append a new element to the queue.\n
    `dequeue()` - Pop the head of the queue.\n
    `peek()` - Return the head of the queue without removing it.\n
    `isEmpty()` - Check if the queue is empty.\n
    `toLinkedList()` - Return the linked list version of the queue.
    """

    # RELATED TESTS
    #   test_initializeQueue()
    def __init__(self):
        """
        Intialize the queue by creating a new linked list instance.
        """
        self.__list = LinkedList()


    def __str__(self) -> str:
        return self.__list.__str__()


    # RELATED TESTS
    #   test_enqueueOne()
    #   test_enqueueMany()
    #   test_enqueueAndDequeue()
    def enqueue(self, item):
        self.__list.append(item)
        pass


    # RELATED TESTS
    #   test_dequeueOne()
    #   test_dequeueMany()
    #   test_dequeueFromAnEmptyList()
    #   test_enqueueAndDequeue()
    def dequeue(self):
        """
        Pop and return the queue of the list.
        """
        return self.__list.pop()

    
    # RELATED TESTS
    #   test_peekPopulatedQueue()
    #   test_peekEmptyQueue()
    def peek(self):
        """
        Return the head of the queue without removing it.
        """
        return self.__list.head()


    # RELATED TESTS
    #   test_populatedIsNotEmpty()
    #   test_unpopulatedIsEmpty()
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
    
    
    # RELATED TESTS
    #   test_toLinkedList()
    def toLinkedList(self) -> LinkedList:
        """
        Return the linked list of the queue.
        """
        return self.__list