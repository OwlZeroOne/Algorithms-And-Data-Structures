class Array:
    """
    A static, homogeneous and efficient data structure - holds a fixed number of like-data that can be accessed directly via address indexing. Current implementation consists of:\n
    `initDirect()` - Instantiate a new array and initialize values through parameters.\n
    `get()` - Retreive item from provided address index.\n
    `set()` - Set item at provided address index.\n
    `size()` - Return the size of the array.\n
    `type()` - Return the type of the array elements.\n
    `extend()` - Extend array by doubling its size and returning a new instance.\n
    `listToArray()` - Convert a provided list to an array and return its instance.\n
    `toList()` - Convert the array to a list and return it.\n
    """
    # RELATED TESTS
    #   test_initializeArray()
    def __init__(self, size: int, type: type):
        """
        Initialize an empty array with a predefined `size` and `type`.
        """
        self.__size = size
        self.__type = type
        self.__addresses = self.__assignSpace()


    def initDirect(*args):
        """
        Directly initialize an array of arbitrary size. Type will be inferred from the `args`.
        """
        arr = Array(len(args), Array.__getType(args))

        for i in range(len(args)):
            arr.set(i, args[i])

        return arr
    

    def __str__(self) -> str:
        
        output = ""

        for i in range(self.__size):
            item = self.get(i)
            output += (str(item) if item != None else "") + ("," if i < self.__size - 1 else "")

        return str.format("[{}]", output)
    

    def get(self, index):
        """
        Return the item at provided index.
        """
        if index >= 0 and index <= self.__size:
            address = str.format("&arr{}", index)
            return self.__addresses[address]
        
        raise IndexError("Array index out of range!")


    # RLATED TESTS
    #   test_setItemAtValidIndexWithValidType()
    #   test_setItemAtIllegalIndexWithValidType()
    #   test_setItemAtValidIndexWithInvalidType()
    def set(self, index, item):
        """
        Set item at provided index.
        """
        if type(item) == self.__type:
            if index >= 0 and index <= self.__size -1:
                address = str.format("&arr{}", index)
                self.__addresses[address] = item
            else:
                raise IndexError("Array index out of range!")
        else:
            raise TypeError("Illegal type for the array!")

    
    # RELATED TESTS
    #   test_initializeArray()
    #   test_setItemAtValidIndexWithValidType()
    def size(self):
        """
        Return the size of the array.
        """
        return self.__size
    

    # RELATED TESTS
    #   test_initializeArray()
    #   test_setItemAtValidIndexWithValidType()
    def type(self):
        """
        Return the type of stored elements.
        """
        return self.__type
    

    # RELATED TESTS
    #   test_extensibleArray()
    def extend(self):
        """
        Provides extending operation if the array needs to be larger. Once invoked, the operation returns a copy of itself, extended by double of its own array's size.
        """
        new_arr = Array(self.__size * 2, self.__type)

        for i in range(self.__size):
            new_arr.set(i, self.get(i))

        return new_arr
    

    # RELATED TESTS
    #   test_convertHomogeneusListToArray()
    #   test_convertHeterogeneusListToArray()
    def listToArray(l:list):
        """
        Convert and a list to an array and return it.
        """
        arr = Array(len(l), Array.__getType(l))

        for i in range(len(l)):
            arr.set(i,l[i])

        return arr
    

    # RELSTED TESTS
    #   test_convertArrayToList()
    def toList(self) -> list:
        """
        Convert this array to a built-in list.
        """
        n = self.__size
        l = [None]*n

        for i in range(n):
            l[i] = self.get(i)

        return l


    def __assignSpace(self):
        """
        Simulate assignment of space and addresses for the array.
        """
        d = dict()
        
        for i in range(self.__size):
            d[str.format("&arr{}",i)] = None

        # print(str.format("{}:{}", self.type(), d))

        return d
    
    
    def __getType(l:list):

        prev_t = type(l[0])
        for i in range(len(l)):
            
            t = type(l[i])
            # print(str.format("{} : {}", prev_t, t))
            if prev_t != t:
                
                raise TypeError(str.format("Incompatible type found at index {}!", i))
            
            prev_t = t

        return t