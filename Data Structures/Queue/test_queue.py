import unittest
from myQueue import *
import _LinkedList

class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.q = Queue()


    def test_initializeQueue(self):
        """
        Attempt to initialize an empty queue. The result should be an object of type `Queue` and size `0`.
        """
        self.assertEqual(type(self.q), Queue)
        self.assertEqual(self.q.size(), 0)

    
    def sampleQueue(multiplier:int) -> Queue:
        q = Queue()
        for i in range(1,11):
            q.enqueue(i*multiplier)

        return q

    def test_enqueueOne(self):
        """
        Enqueue one element to an empty queue. The resulting queue must have one element.
        """
        self.q.enqueue(1)
        
        self.assertEqual(self.q.size(), 1)
        self.assertEqual(str(self.q), "[1]")


    def test_peekPopulatedQueue(self):
        """
        Peek head element of the queue. The first item in the queue should be returned.
        """
        self.q = TestQueue.sampleQueue(7)
        self.assertEqual(self.q.peek(), 7)


    def test_peekEmptyQueue(self):
        """
        Attempt to peek an element from an empty queue. `None` should be returned.
        """
        self.assertIsNone(self.q.peek())


    def test_enqueueMany(self):
        """
        Enqueue several values into the queue.
        """
        self.q = TestQueue.sampleQueue(6)

        self.assertEqual(self.q.size(), 10)
        self.assertEqual(str(self.q), "[6,12,18,24,30,36,42,48,54,60]")


    def test_dequeueOne(self):
        """
        Dequeue an element from a populated queue. The head element should be returned and the resultant queueue should have a new head.
        """
        self.q = TestQueue.sampleQueue(multiplier=8)
        deq = self.q.dequeue()

        self.assertEqual(deq, 8)
        self.assertEqual(self.q.peek(), 16)
        self.assertEqual(str(self.q),"[16,24,32,40,48,56,64,72,80]")


    def test_dequeueMany(self):
        """
        Dequeue many elements from the queue.
        """
        # [4,8,12,16,20,24,28,32,26,40]
        self.q = TestQueue.sampleQueue(4)
        
        for i in range(5):
            deq = self.q.dequeue()

        self.assertEqual(deq, 20)
        self.assertEqual(self.q.peek(),24)
        self.assertEqual(str(self.q),"[24,28,32,36,40]")


    def test_dequeueFromAnEmptyQueue(self):
        """
        Attempt to dequeue from an empty list. An `EmptyListException` should be thrown by the `LinkedList` module.
        """
        with self.assertRaises(_LinkedList.EmptyListException):
            self.q.dequeue()


    def test_enqueueAndDequeue(self):
        """
        Attempt to enqueue and dequeue a few of times.
        """
        q = self.q

        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        q.enqueue('d')
        q.enqueue('e')

        self.assertEqual(q.size(), 5)
        self.assertEqual(q.peek(), 'a')
        self.assertEqual(str(q), "[a,b,c,d,e]")

        q.dequeue()
        q.dequeue()
        deq = q.dequeue()

        self.assertEqual(q.size(), 2)
        self.assertEqual(deq, 'c')
        self.assertEqual(q.peek(), 'd')
        self.assertEqual(str(q), "[d,e]")


    def test_populatedIsNotEmpty(self):
        """
        Check if a populated list is empty. The result should be `False`.
        """
        self.q = TestQueue.sampleQueue(3)

        self.assertFalse(self.q.isEmpty())


    def test_unpopulatedIsEmpty(self):
        """
        Check if an unpopulated list is empty. The result should be `True`.
        """
        self.assertTrue(self.q.isEmpty())


    def test_toLinkedList(self):
        """
        Attempt to convert the que to a `LinkedList`. The result should be a linked list of the same size as the `Queue`, with `head()` the same as `peek()`.
        """
        self.q = TestQueue.sampleQueue(2)
        ll = self.q.toLinkedList()

        self.assertEqual(type(ll), LinkedList)
        self.assertNotEqual(type(ll), Queue)
        self.assertEqual(self.q.peek(), ll.head())
        self.assertEqual(self.q.size(), ll.size())
        self.assertEqual(ll.size(), 10)




if __name__ == "__main__":
    unittest.main()