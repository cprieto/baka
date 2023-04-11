from baka.chap06 import BSTree


def test_bstee():
    t = BSTree()
    assert not t.root

    t.append(5)
    assert t.root
    assert t.root.data == 5

    t.append(3)
    assert t.root.left
    assert t.root.left.data == 3

    t.append(6)
    assert t.root.right
    assert t.root.right.data == 6

    t.append(12)
    assert t.root.right.right
    assert t.root.right.right.data == 12