from baka.chap05 import Stack, Queue


def test_stack_push_pop_peek():
    s = Stack()
    assert s.size == 0

    s.push('a')
    assert s.size == 1

    s.push('b')
    assert s.size == 2

    assert s.peek() == 'b'
    assert s.size == 2

    assert s.pop() == 'b'
    assert s.size == 1

    assert s.peek() == 'a'
    assert s.size == 1

    assert s.pop() == 'a'
    assert s.size == 0


def test_queue_enqueue_dequeue():
    q = Queue()
    assert q.size == 0

    q.enqueue('a')
    assert q.size == 1

    q.enqueue('b')
    assert q.size == 2

    q.enqueue('c')
    assert q.size == 3

    assert q.dequeue() == 'a'
    assert q.size == 2

    assert q.dequeue() == 'b'
    assert q.size == 1

    assert q.dequeue() == 'c'
    assert q.size == 0
