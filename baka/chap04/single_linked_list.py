from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next: Optional[Node[T]] = None

    def __str__(self):
        return f"{self.data} -> {str(self.next) if self.next else 'NULL'}"


class SingleLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    def __str__(self):
        if not self.head:
            return 'Empty'
        return str(self.head)

    def append(self, data: T):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def __iter__(self):
        if not self.head:
            return

        current = self.head
        while current:
            yield current.data
            current = current.next
        return

    def delete(self, data: T):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self._size -= 1
                return

            prev = current
            current = current.next
