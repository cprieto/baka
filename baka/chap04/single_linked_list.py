from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __int__(self, data: T):
        self.data = data
        self.next: Optional[Node[T]] = None

    def __str__(self):
        next_node = "NULL" if self.next else str(self.next)
        return f'{self.data} -> {next_node}'


class SingleLinkedList(Generic[T]):
    def __int__(self):
        self.tail: Optional[Node[T]] = None

    def append(self, data: T):
        pass
