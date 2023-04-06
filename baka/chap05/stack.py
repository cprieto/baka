from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next: Optional[Node[T]] = None


class Stack(Generic[T]):
    def __init__(self):
        self.top: Optional[Node[T]] = None
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    def push(self, data: T):
        node = Node(data)
        if self.top:
            node.next = self.top

        self.top = node
        self._size += 1

    def pop(self) -> T:
        current = self.top
        self.top = self.top.next if self.top else None
        if current:
            self._size -= 1
            return current.data
        return None

    def peek(self) -> T:
        return self.top.data if self.top else None
