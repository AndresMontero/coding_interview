import time
import threading

from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)  # sames as insert(0)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


def place_order(orders, queue):
    for order in orders:
        print(f"Adding order {order}, queue is {queue.size()}\n")
        queue.enqueue(order)
        time.sleep(0.5)


def serve_order(queue):
    time.sleep(1)
    while queue.size() > 0:
        print(f"Popping order {queue.dequeue()} queue is {queue.size()}\n")
        time.sleep(2)


orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
queue = Queue()

t1 = threading.Thread(target=place_order, args=(orders, queue))
t2 = threading.Thread(target=serve_order, args=(queue,))

t1.start()
t2.start()

t1.join()
t2.join()
