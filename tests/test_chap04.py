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
