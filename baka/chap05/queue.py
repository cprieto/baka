from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next: Optional[Node[T]] = None

class Queue(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    def enqueue(self, data: T):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def dequeue(self) -> T:
        current = self.head
        if not current:
            return None

        if self.head == self.tail:
            self.tail = None

        self.head = current.next
        self._size -= 1
        return current.data
