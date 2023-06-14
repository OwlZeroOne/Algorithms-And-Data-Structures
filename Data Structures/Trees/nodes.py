class Node:

    key = parent = None

    def __init__(self, key, parent) -> None:
        self.key = key
        self.parent = parent


class BinaryNode(Node):

    left = right = None

    def __init__(self, key, parent) -> None:
        super().__init__(key, parent)


class RedBlackNode(BinaryNode):
    """
    Node for a red-black tree. Inherits the key, left and right from `BinaryNode`, in addition to the `color` of the node which must be either `red`  or `black`.
    """
    color = None

    def __init__(self, key, parent, color) -> None:

        if not(color == "red" or color == "black"):
            raise ValueError("Color of the node must be either \"red\" or \"black\"!")
        
        super().__init__(key, parent)
        self.color = color