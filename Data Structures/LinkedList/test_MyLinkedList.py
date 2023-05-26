import unittest
from MyLinkedList import *

class TestNode(unittest.TestCase):

    def header(func_name: str):
        print("=============================================")
        print("=--> " + func_name)


    def footer():
        print("=--> END")
        print("=============================================")


    def test_createNode(self):
        """
        Attempt to create a node. Returned type should be `Node`.
        """
        # TestNode.header("Create Node")

        new_node = Node('a')
        self.assertEqual(type(new_node), Node)
        # print(str.format("{} == {}", type(new_node), Node))

        # TestNode.footer()


    def test_nodeValue(self):
        """
        Test node value, which should be obtainable from Node.item.
        """
        # TestNode.header("Node Value")

        node = Node('g')
        self.assertEqual(node.item, 'g')
        # print(str.format("{} == {}", node.item, 'g'))

        # TestNode.footer()

    
    def test_nodeLinks(self):
        """
        Test node links, which should link up once referenced by some other node.
        """
        # TestNode.header("Node Links")
        prev = Node("Node 1")
        next = Node("Node 3")
        this = Node("Node 2", prev, next)

        self.assertEqual(prev.next, this)
        self.assertIsNone(prev.previous)

        # print(str.format("Previous: {}", prev))
        # print(str.format(".next: {}", prev.next))
        # print(str.format(".previous: {}\n", prev.previous))

        self.assertEqual(this.previous, prev)
        self.assertEqual(this.next, next)

        # print(str.format("This: {}", this))
        # print(str.format(".next: {}", this.next))
        # print(str.format(".previous: {}\n", this.previous))

        self.assertEqual(next.previous, this)
        self.assertIsNone(next.next)

        # print(str.format("Next: {}", next))
        # print(str.format(".next: {}", next.next))
        # print(str.format(".previous: {}\n", next.previous))

        # TestNode.footer()


    def test_equality(self):
        """
        Check for value equality between two nodes.
        """
        n1 = Node(56)
        n2 = Node('56')
        n3 = Node(56)

        self.assertFalse(n1.equals(n2))
        self.assertTrue(n1.equals(n3))


    def test_toString(self):
        """
        Check whether toString returns the stringified value of `Node.item`.
        """
        n = Node("Sample value")

        self.assertEqual(n.item, "Sample value")
        



class TestLinkedList(unittest.TestCase):
    
    
    def setUp(self) -> None:
        self.ll = LinkedList()


    def test_initializeList(self):
        """
        Iitialize a new linked list. Result should be a `LinkedList` type.
        """
        self.assertEqual(type(self.ll), LinkedList)


    def __listSate(self, expected_size:int, expected_string:str):
        self.assertEqual(self.ll.size(), expected_size)
        self.assertEqual(str(self.ll), expected_string)


    def test_initialListSizeIsZero(self):
        """
        A new instance of the linked list should be an empty list with a no head nor tail.
        """
        self.assertIsNone(self.ll.head())
        self.assertIsNone(self.ll.tail())
        TestLinkedList.__listSate(self, 0, "[]")


    def test_appendOne(self):
        """
        Attempt to append one item to an empty list. The final result should have one element with it being both the head and the tail of the list.
        """
        val = "Some Value"

        self.ll.append(val)
        TestLinkedList.__listSate(self, 1, "["+val+"]")
        self.assertEqual(self.ll.head(), self.ll.tail())


    def test_appendMany(self):
        """
        Attempt to append many items to an empty list. Head should be first element of the list and tail should be last.
        """
        for i in range(1,11):
            self.ll.append(i*4)

        # print(self.ll)
        TestLinkedList.__listSate(self, 10, "[4,8,12,16,20,24,28,32,36,40]")
        self.assertEqual(self.ll.head(), 4)
        self.assertEqual(self.ll.tail(), 40)

    
    def test_appendStrings(self):
        """
        Attempt to append a few strings onto an empty list.
        """
        self.ll.append("My")
        self.ll.append("Name")
        self.ll.append("Is")
        self.ll.append("Matty")

        TestLinkedList.__listSate(self, 4, "[My,Name,Is,Matty]")
        self.assertEqual(self.ll.head(), 'My')
        self.assertEqual(self.ll.tail(), 'Matty')


    def test_prependOne(self):
        """
        Attempt to prepend a single item to an empty list. The final result should have one element with it being both the head and the tail of the list.
        """
        val = "Some Value"

        self.ll.prepend(val)
        TestLinkedList.__listSate(self, 1, "["+val+"]")
        self.assertEqual(self.ll.head(), self.ll.tail())


    def test_prependMany(self):
        """
        Attempt to prepend many items to the list. Head should be first element of the list and tail should be last.
        """
        for i in range(1,11):
            self.ll.prepend(i*4)

        # print(self.ll)
        TestLinkedList.__listSate(self, 10, "[40,36,32,28,24,20,16,12,8,4]")
        self.assertEqual(self.ll.head(), 40)
        self.assertEqual(self.ll.tail(), 4)


    def test_alternateAppendAndPrepend(self):
        """
        Attempt to both append and prepend items to a prepopulated list. `append()` should add to the right side of the list, while `prepend()` adds to left side of it.
        """
        self.ll.append(0)

        # Add exact tens to the right of 0. Any fives go to the left
        for i in range(1,11):
            self.ll.append(i*5) if i%2==0 else self.ll.prepend(i*5)

        TestLinkedList.__listSate(self, 11, "[45,35,25,15,5,0,10,20,30,40,50]")


    def test_buildListOfTenNumbers(self):
        """
        Attempt to build a linked list of numbers from the built-in `list` type.
        """
        l = [1,2,3,4,5,6,7,8,9,10]
        self.ll.buildFrom(l)

        TestLinkedList.__listSate(self, 10, "[1,2,3,4,5,6,7,8,9,10]")


    def test_buildListOfTenStrings(self):
        """
        Attempt to build a linked list of strings from the built-in `list` type.
        """
        l = ['A','long','time','ago','in','a','galaxy','far','far','away']
        self.ll.buildFrom(l)

        TestLinkedList.__listSate(self, 10, "[A,long,time,ago,in,a,galaxy,far,far,away]")


    def test_buildEmptyList(self):
        """
        Attempt to build an empty list. Should successfully do so.
        """
        self.ll.buildFrom([])

        TestLinkedList.__listSate(self, 0, "[]")


    def test_popOne(self):
        """
        Attempt to pop a single item from the list. The popped item should be the head of the list and the new head should be the second element in the list.
        """
        self.ll.buildFrom([9,1,2,3,4])
        head = self.ll.head()
        pop = self.ll.pop()

        TestLinkedList.__listSate(self, 4, "[1,2,3,4]")
        self.assertEqual(pop, head)
        self.assertEqual(self.ll.head(), 1)


    def test_popMany(self):
        """
        Attempt to pop many items from the list. New element at the head should be found.
        """
        self.ll.buildFrom(['One','Two','Three','Four','Five',6,7,8,9,10])

        for i in range(5):
            pop = self.ll.pop()

        TestLinkedList.__listSate(self, 5, "[6,7,8,9,10]")
        self.assertEqual(pop, 'Five')
        self.assertEqual(self.ll.head(), 6)
        # print(self.ll)


    def test_popFromEmptyList(self):
        """
        Attempt to pop from an empty list. Should raise a user-defined `EmptyListException`.
        """
        assert self.ll.size() == 0, "List size is not 0!"

        with self.assertRaises(EmptyListException):
            self.ll.pop()


    def test_dropOne(self):
        """
        Attempt to drop a single item from the list. The dropped item should be the tail of the list and the new tail should be the second-last element in the list.
        """
        self.ll.buildFrom([1,2,3,4,9])
        tail = self.ll.tail()
        drop = self.ll.drop()

        TestLinkedList.__listSate(self, 4, "[1,2,3,4]")
        self.assertEqual(drop, tail)
        self.assertEqual(self.ll.tail(), 4)


    def test_dropMany(self):
        """
        Attempt to drop many items from the list. New element at the tail should be found.
        """
        self.ll.buildFrom([6,7,8,9,10,'One','Two','Three','Four','Five'])

        for i in range(5):
            drop = self.ll.drop()

        TestLinkedList.__listSate(self, 5, "[6,7,8,9,10]")
        self.assertEqual(drop, 'One')
        self.assertEqual(self.ll.tail(),10)
        # print(self.ll)


    def test_dropFromEmtyList(self):
        """
        Attempt to drop from an empty list. Should raise a user-defined `EmptyListException`.
        """
        assert self.ll.size() == 0, "List size is not 0!"

        with self.assertRaises(EmptyListException):
            self.ll.drop()


    def test_alternatePopAndDrop(self):
        """
        Attempt to both pop and drop items from a prepopulated list. `drop()` should remove from the right side of the list, while `pop()` removes from the left side of it.
        """
        self.ll.buildFrom([45,35,25,15,5,0,10,20,30,40,50])

        for i in range(10):
            if i%2==0:
                pop = self.ll.pop()
            else:
                drop = self.ll.drop()

        TestLinkedList.__listSate(self, 1, "[0]")
        self.assertEqual(pop, 5)
        self.assertEqual(drop, 10)


    def test_AppendPrependPopAndDrop(self):
        """
        Combine `append()`, `prepend()`, `pop()` and `drop()`.
        """
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

        TestLinkedList.__listSate(self, 3, "[1,2,3]")

        self.ll.prepend(4)
        self.ll.prepend(5)
        self.ll.prepend(6)

        TestLinkedList.__listSate(self, 6, "[6,5,4,1,2,3]")

        self.ll.pop()
        pop = self.ll.pop()

        TestLinkedList.__listSate(self, 4, "[4,1,2,3]")

        self.ll.drop()
        drop = self.ll.drop()

        TestLinkedList.__listSate(self, 2, "[4,1]")
        self.assertEqual(drop, 2)
        self.assertEqual(pop, 5)


    def test_removeItemAtGivenIndex(self):
        """
        Attempt to remove a valid item from the list. The removed item should be returned.
        """
        self.ll.buildFrom([1,2,3,6,4,5])

        remove = self.ll.remove(6)

        TestLinkedList.__listSate(self, 5, "[1,2,3,4,5]")
        self.assertEqual(remove, 6)


    def test_removeNonExistentItemFromTheList(self):
        """
        Attempt to remove an element that is not contained within the list. Should raise a `RuntimeError` exception.
        """
        self.ll.buildFrom([1,2,3,6,4,5])

        with self.assertRaises(RuntimeError):
            self.ll.remove(8)
            

    def test_getElementAtIndex(self):
        """
        Attempt to retrieve an element at a valid index.
        """
        self.ll.buildFrom([1,2,3,6,4,5])

        self.assertEqual(self.ll.getAt(3), 6)

    
    def test_getElementAtNegativeIndex(self):
        """
        Attempt to retrieve an element at a negative index. Should raise an `IndexError` exception.
        """
        self.ll.buildFrom([1,2,3,6,4,5])

        with self.assertRaises(IndexError):
            self.ll.getAt(-1)


    def test_getElementAtIndexEqualToSize(self):
        """
        Attempt to retrieve an element at index equal to size of the list. Should raise an `IndexError` exception.
        """
        self.ll.buildFrom([1,2,3,6,4,5])

        with self.assertRaises(IndexError):
            self.ll.getAt(6)


    def test_getElementAtIndexGreaterThanSize(self):
        """
        Attempt to retrieve an element at index greater than size of the list. Should raise an `IndexError` exception.
        """
        self.ll.buildFrom([1,2,3,6,4,5])

        with self.assertRaises(IndexError):
            self.ll.getAt(10)


    def test_removeElementAtValidIndex(self):
        """
        Attempt to remove an item from an arbitrary, valid index. Should return the removed item.
        """
        ll = self.ll
        ll.buildFrom([1,2,3,6,4,5])

        item = ll.remove(ll.getAt(3))
        TestLinkedList.__listSate(self, 5, "[1,2,3,4,5]")
        self.assertEqual(item, 6)


    def test_removeElmentAtInvalidIndex(self):
        """
        Attempt to remove an item at an invalid index. Should raise an `IndexError` exception.
        """
        ll = self.ll
        ll.buildFrom([1,2,3,6,4,5])

        with self.assertRaises(IndexError):
            ll.remove(ll.getAt(-1))

        with self.assertRaises(IndexError):
            ll.remove(ll.getAt(6))

        with self.assertRaises(IndexError):
            ll.remove(ll.getAt(7))


    def test_unpopulatedListIsEmpty(self):
        """
        Check if an unpopulated list is empty. Should be empty.
        """
        self.assertTrue(self.ll.isEmpty())


    def test_populatedListIsNotEmpty(self):
        """
        Check if a populated list is empty. Should not be empty.
        """
        self.ll.buildFrom(['1',2,False,"hi"])
        self.assertFalse(self.ll.isEmpty())


    def test_CompareTheSameLists(self):
        """
        Comapre two different objects of lists to see if they have equal values. Values different and same objects should match.
        """
        ll1 = self.ll
        ll1.buildFrom(['a','b','c',4,5,6])
        ll2 = LinkedList()
        ll2.buildFrom(['a','b','c',4,5,6])

        self.assertTrue(ll1.equals(ll2))
        self.assertTrue(ll2.equals(ll1))
        self.assertTrue(ll2.equals(ll2))
        self.assertTrue(ll1.equals(ll1))


    def test_CompareDifferentLists(self):
        """
        Comapre two different objects of lists to see if they have equal values. Values of the two lists should not match.
        """
        ll1 = self.ll
        ll1.buildFrom(['a','b','c',4,5,6])
        ll2 = LinkedList()
        ll2.buildFrom(['a','b','c','d','e','f'])

        self.assertFalse(ll1.equals(ll2))
        self.assertFalse(ll2.equals(ll1))


    def test_CompareListsOfDifferentSizes(self):
        """
        Compare lists of different sizes to check if they have equal values. Should return false due to incompatible list lengths.
        """
        ll1 = self.ll
        ll1.buildFrom(['a','b','c'])
        ll2 = LinkedList()
        ll2.buildFrom(['a','b','c','d','e','f'])

        self.assertFalse(ll1.equals(ll2))
        self.assertFalse(ll2.equals(ll1))


    def test_sortAscending(self):
        """
        Sort the list in ascending order.
        """
        self.ll.buildFrom([12,56,34,90,12,2,9,87])
        self.ll.sort()

        self.assertEqual(str(self.ll), "[2,9,12,12,34,56,87,90]")


    def test_sortDecending(self):
        """
        Sort the list in decending order.
        """
        self.ll.buildFrom([12,56,34,90,12,2,9,87])
        self.ll.sort("dec")

        self.assertEqual(str(self.ll), "[90,87,56,34,12,12,9,2]")


    def test_sortEmptyList(self):
        """
        Attempt to sort an empty list. Final list should remain empty.
        """
        self.ll.sort()

        self.assertEqual(str(self.ll), "[]")


    def test_sortSortedList(self):
        """
        Attempt to sort an already sorted list. Final result should be the same as the original list.
        """
        self.ll.buildFrom([2,9,12,12,34,56,87,90])
        self.ll.sort()

        self.assertEqual(str(self.ll), "[2,9,12,12,34,56,87,90]")


    def test_sortInvalidOrder(self):
        """
        Attempt to sort the list in an invalid order. Should raise a `ValueError` exception.
        """
        self.ll.buildFrom([12,56,34,90,12,2,9,87])
        
        with self.assertRaises(ValueError):
            self.ll.sort("MyOrder")


    def test_clonePrepopulatedList(self):
        """
        Create a replica object of a populated list. Lists should be different objects, but should be comparable and should be the same.
        """

        self.ll.buildFrom(['a','b','c','d','e','f'])

        ll_copy = self.ll.clone()
        # print(self.ll)
        # print(ll_copy)

        self.assertNotEqual(self.ll, ll_copy)
        self.assertTrue(self.ll.equals(ll_copy))
        self.assertTrue(ll_copy.equals(self.ll))


    def test_cloneUpopulatedList(self):
        """
        Create a replica object of an empty list. Lists should be different objects, but should be comparable and should be the same.
        """

        self.ll.buildFrom([])

        ll_copy = self.ll.clone()

        self.assertNotEqual(self.ll, ll_copy)
        self.assertTrue(self.ll.equals(ll_copy))
        self.assertTrue(ll_copy.equals(self.ll))


    def test_getValidSublist(self):
        """
        Get a new list object that is a sublist of this list. The data type should be `LinkedList` and should not be of the same reference as this one.
        """
        ll = self.ll
        ll.buildFrom([1,2,3,4,5,6,7,8,9,10])
        sub = ll.sublist(3,8)

        self.assertEqual(type(sub), LinkedList)
        self.assertNotEqual(sub, ll)
        self.assertEqual(sub.size(), 6)
        self.assertEqual(str(sub), "[4,5,6,7,8,9]")


    def test_getSublistFromNegativeToValidIndex(self):
        """
        Attempt to get a sublist starting from a negative index. Should raise an `IndexError` exception.
        """
        ll = self.ll
        ll.buildFrom([1,2,3,4,5,6,7,8,9,10])
        
        with self.assertRaises(IndexError):
            ll.sublist(-2,5)


    def test_getSublistFromValidToOutOfRangeIndex(self):
        """
        Attempt to get a sublist ending at an index "out-of-bounds". Should raise an `IndexError` exception.
        """
        ll = self.ll
        ll.buildFrom([1,2,3,4,5,6,7,8,9,10])
        
        with self.assertRaises(IndexError):
            ll.sublist(5,10)

        with self.assertRaises(IndexError):
            ll.sublist(5,11)

    
    def test_getSublistOfEmptyList(self):
        """
        Attempt to get a sublist from an empty list. An empty list should be returned.
        """
        ll = self.ll
        ll.buildFrom([])
        sub = ll.sublist(0,0)
        
        self.assertEqual(type(sub), LinkedList)
        self.assertNotEqual(sub, ll)
        self.assertEqual(sub.size(), 0)
        self.assertEqual(str(sub), "[]")


    def test_getSublistOfAnotherSublist(self):
        """
        Attempt to get a sublist of a sublist of the original list. Type should be `LinkedList` and should not be the same object as the original or the first sublist.
        """
        ll = self.ll
        ll.buildFrom([1,2,3,4,5,6,7,8,9,10])
        sub = ll.sublist(2,7)

        self.assertEqual(type(sub), LinkedList)
        self.assertNotEqual(sub, ll)
        self.assertEqual(sub.size(), 6)
        self.assertEqual(str(sub), "[3,4,5,6,7,8]")

        subsub = sub.sublist(2,3)

        self.assertEqual(type(subsub), LinkedList)
        self.assertNotEqual(subsub, ll)
        self.assertNotEqual(subsub, sub)
        self.assertEqual(subsub.size(), 2)
        self.assertEqual(str(subsub), "[5,6]")




if __name__ == "__main__":
    unittest.main()