import unittest
from myArray import *

class TestArray(unittest.TestCase):
    """
    An array is a fixed-size collection of data of the same type. The only way to enlarge an array is by array extension. Main features of a typical array are item assignment and retreival at index, iteration of indexes, and constant assignment and retreival time, but runtime analysis will be omitted in this scope.
    """

    def test_initializeArray(self):
        "Initializing an array should pass a size and a type. Which should be returned by `Array.size()` and `Array.type()`. Test is applied on types `str`, `int` and `list`."
        arrInt = Array(5, int)
        arrStr = Array(5, str)
        arrList = Array(5, list)

        self.assertEqual(arrInt.size(), 5)
        self.assertEqual(arrStr.size(), 5)
        self.assertEqual(arrList.size(), 5)

        self.assertEqual(arrInt.type(), int)
        self.assertEqual(arrStr.type(), str)
        self.assertEqual(arrList.type(), list)


    def test_intializeArrayDirectly(self):
        
        arrInt = Array.initDirect(1,2,3,4,5)

        self.assertEqual(arrInt.size(), 5)
        self.assertEqual(arrInt.type(), int)
        self.assertEqual(str(arrInt), "[1,2,3,4,5]")


    def test_setItemAtValidIndexWithValidType(self):
        """
        Set item at provided index with a compatible data type. Should successfully assign value to the index.
        """
        arrInt = Array(5, int)

        arrInt.set(0, 1)
        arrInt.set(1, 3)
        arrInt.set(2, 5)
        arrInt.set(3, 7)
        arrInt.set(4, 9)

        self.assertEqual(arrInt.size(), 5)
        self.assertEqual(arrInt.type(), int)
        self.assertEqual(str(arrInt), "[1,3,5,7,9]")


    def test_setItemAtIllegalIndexWithValidType(self):
        """
        Attempt to set an item at illegal index, but valid type. An `IndexError` exception should be thrown.
        """
        arrStr = Array(3, str)

        with self.assertRaises(IndexError):
            arrStr.set(-1, "negIndex")

        with self.assertRaises(IndexError):
            arrStr.set(3, "index=size")

        with self.assertRaises(IndexError):
            arrStr.set(4, "bigIndex")


    def test_setItemAtValidIndexWithInvalidType(self):
        """
        Attempt to set an item at a valid index, but an illegal type. A `TypeError` exception should be returned.
        """
        arrStr = Array(3, str)

        with self.assertRaises(TypeError):
            arrStr.set(0, 1)

        with self.assertRaises(TypeError):
            arrStr.set(1, False)

        with self.assertRaises(TypeError):
            arrStr.set(2, [1,2,3])


    def test_extensibleArray(self):
        """
        Attempt to extend the array by doubling its size in order to accommodate more elemnts.
        """
        arrInt = Array(3, int)

        arrInt.set(0,1)
        arrInt.set(1,3)
        arrInt.set(2,5)

        self.assertEqual(arrInt.size(), 3)
        self.assertEqual(arrInt.type(), int)
        self.assertEqual(str(arrInt), "[1,3,5]")

        with self.assertRaises(IndexError):
            arrInt.set(3,7)

        arrInt = arrInt.extend()
        
        self.assertEqual(arrInt.size(), 6)
        self.assertEqual(arrInt.type(), int)
        self.assertEqual(str(arrInt), "[1,3,5,,,]")

        arrInt.set(3,7)

        self.assertEqual(str(arrInt), "[1,3,5,7,,]")


    def test_twoDimensionalArray(self):
        """
        Attempt to create and manipulate a two-dimensional array (aka. a matrix).
        """
        arr2D = Array(5, Array)
        counter = 1

        for i in range(5):
            arr2D.set(i, Array(5, int))
            for j in range(5):
                arr2D.get(i).set(j,counter)
                counter += 1

        self.assertEqual(arr2D.size(), 5)
        self.assertEqual(arr2D.type(), Array)

        for i in range(5):
            sub_arr = arr2D.get(i)

            self.assertEqual(sub_arr.size(), 5)
            self.assertEqual(sub_arr.type(), int)
            # print(sub_arr)

        # print(arr2D)


    def test_convertHomogeneusListToArray(self):
        """
        Convert a built-in, homogeneus list to an array object. Successful conversion expected.
        """
        l = [1,2,3,4,5]
        arr = Array.listToArray(l)

        self.assertEqual(arr.size(), 5)     
        self.assertEqual(arr.type(), int)
        self.assertEqual(str(arr), "[1,2,3,4,5]")


    def test_convertHeterogeneusListToArray(self):
        """
        Convert a built-n, heterogeneus list to an array object. `TypeError` exception should be thrown.
        """
        l = [1,2,'three',4,5]
        
        with self.assertRaises(TypeError):
            Array.listToArray(l)


    def test_convertArrayToList(self):
        """
        Convert an array to a built-in type list.
        """
        arr = Array.initDirect(1,2,3,4,5)

        l = arr.toList()

        self.assertEqual(l, [1,2,3,4,5])




if __name__ == "__main__":
    unittest.main()