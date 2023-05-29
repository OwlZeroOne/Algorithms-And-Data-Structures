import unittest
from myStack import *
import _LinkedList

class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack()


    def test_initializeStack(self):
        """
        Attempt to initialize an empty stack. The result should be an object of type `Stack` and size `0`.
        """
        self.assertEqual(type(self.stack), Stack)
        self.assertEqual(self.stack.size(), 0)


    def sampleStack(multiplier:int) -> Stack:
        stack = Stack()
        for i in range(1,11):
            stack.append(i*multiplier)

        return stack


    def test_appendOne(self):
        """
        Append one element to an empty stack. The resulting stack must have one element.
        """
        self.stack.append(1)
        
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(str(self.stack), "[1]")


    def test_peekPopulatedStack(self):
        """
        Peek tail element of the stack. The last item in the stack should be returned.
        """
        self.stack = TestStack.sampleStack(7)
        self.assertEqual(self.stack.peek(), 70)


    def test_peekEmptyStack(self):
        """
        Attempt to peek an element from an empty stack. `None` should be returned.
        """
        self.assertIsNone(self.stack.peek())


    def test_appendMany(self):
        """
        Append several values into the stack.
        """
        self.stack = TestStack.sampleStack(6)

        self.assertEqual(self.stack.size(), 10)
        self.assertEqual(str(self.stack), "[6,12,18,24,30,36,42,48,54,60]")


    def test_dropOne(self):
        """
        Drop an element from a populated stack. The tail element should be returned and the resultant stack should have a new tail.
        """
        self.stack = TestStack.sampleStack(multiplier=8)
        drop = self.stack.drop()

        self.assertEqual(drop, 80)
        self.assertEqual(self.stack.peek(), 72)
        self.assertEqual(str(self.stack),"[8,16,24,32,40,48,56,64,72]")


    def test_dropMany(self):
        """
        Drop many elements from the stack.
        """
        # [4,8,12,16,20,24,28,32,26,40]
        self.stack = TestStack.sampleStack(4)
        
        for i in range(5):
            drop = self.stack.drop()

        self.assertEqual(drop, 24)
        self.assertEqual(self.stack.peek(),20)
        self.assertEqual(str(self.stack),"[4,8,12,16,20]")


    def test_dropFromAnEmptyStack(self):
        """
        Attempt to drop from an empty list. An `EmptyListException` should be thrown by the `LinkedList` module.
        """
        with self.assertRaises(_LinkedList.EmptyListException):
            self.stack.drop()

    
    def test_appendAndDrop(self):
        """
        Attempt to append and drop a few of times.
        """
        stack = self.stack

        stack.append('a')
        stack.append('b')
        stack.append('c')
        stack.append('d')
        stack.append('e')

        self.assertEqual(stack.size(), 5)
        self.assertEqual(stack.peek(), 'e')
        self.assertEqual(str(stack), "[a,b,c,d,e]")

        stack.drop()
        stack.drop()
        drop = stack.drop()

        self.assertEqual(stack.size(), 2)
        self.assertEqual(drop, 'c')
        self.assertEqual(stack.peek(), 'b')
        self.assertEqual(str(stack), "[a,b]")


    def test_populatedIsNotEmpty(self):
        """
        Check if a populated stack is empty. The result should be `False`.
        """
        self.stack = TestStack.sampleStack(3)

        self.assertFalse(self.stack.isEmpty())


    def test_unpopulatedIsEmpty(self):
        """
        Check if an unpopulated stack is empty. The result should be `True`.
        """
        self.assertTrue(self.stack.isEmpty())


    def test_toLinkedList(self):
        """
        Attempt to convert the stack to a `LinkedList`. The result should be a linked list of the same size as the `Stack`, with `tail()` the same as `peek()`.
        """
        self.stack = TestStack.sampleStack(2)
        ll = self.stack.toLinkedList()

        self.assertEqual(type(ll), LinkedList)
        self.assertNotEqual(type(ll), Stack)
        self.assertEqual(self.stack.peek(), ll.tail())
        self.assertEqual(self.stack.size(), ll.size())
        self.assertEqual(ll.size(), 10)

    


if __name__ == "__main__":
    unittest.main()
