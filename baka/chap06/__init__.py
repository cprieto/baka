from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.left: Optional[Node[T]] = None
        self.right: Optional[Node[T]] = None

    def insert(self, data: T):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def has_value(self, data: T) -> bool:
        if self.data == data:
            return True
        elif data < self.data:
            return self.left and self.left.has_value(data)
        elif data > self.data:
            return self.right and self.right.has_value(data)

        return False


class BSTree(Generic[T]):
    def __init__(self):
        self.root: Optional[Node[T]] = None

    def append(self, value: T):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)

    def has_value(self, value: T) -> bool:
        return self.root and self.root.has_value(value)

    def delete(self, value):
        pass
