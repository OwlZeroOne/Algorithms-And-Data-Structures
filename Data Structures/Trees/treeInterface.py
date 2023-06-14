from nodes import Node


class TreeInterface:

    N = Node

    def insert(self, key, parent=None) -> None:
        """
        Insert `key` into the tree.
        """
        pass


    def delete(self, key) -> N:
        """
        Delete `key` from the tree.
        """
        pass


    def lookup(self, key) -> N:
        """
        Find node of given key.
        """
        pass


    def toList(self) -> list:
        """
        Return the list version of th tree.
        """
        pass


    def toString(self) -> str:
        """
        Return the string version of the tree in list format.
        """
        pass