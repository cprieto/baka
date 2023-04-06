from baka.chap04.single_linked_list import Node, SingleLinkedList


def test_node_list_to_str():
    n1 = Node('eggs')
    assert str(n1) == 'eggs -> NULL'

    n1.next = Node('ham')
    assert str(n1) == 'eggs -> ham -> NULL'


def test_single_linked_list_append():
    ll = SingleLinkedList()
    ll.append(1)
    assert str(ll) == '1 -> NULL'

    ll.append(2)
    assert str(ll) == '1 -> 2 -> NULL'

    ll.append(3)
    assert str(ll) == '1 -> 2 -> 3 -> NULL'


def test_single_linked_list_size():
    ll = SingleLinkedList()
    ll.append('a')
    ll.append('b')
    ll.append('c')

    assert ll.size == 3


def test_single_linked_list_iter():
    ll = SingleLinkedList()
    ll.append('a')
    ll.append('b')
    ll.append('c')

    elems = list(ll)
    assert elems == ['a', 'b', 'c']


def test_single_linked_list_delete():
    ll = SingleLinkedList()
    ll.delete(100)

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.delete(100)
    assert list(ll) == [1, 2, 3, 4, 5]

    ll.delete(2)
    assert list(ll) == [1, 3, 4, 5]

    ll.delete(1)
    assert list(ll) == [3, 4, 5]

    ll.delete(5)
    assert list(ll) == [3, 4]


def test_single_list_search():
    ll = SingleLinkedList()
    ll.append(3)
    ll.append(12)
    ll.append(5)

    assert not ll.search(100)
    assert ll.search(5)
