# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        # Time O(n)
        # Space O(1)
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.siftDown(current_idx, len(array) - 1, array)
        return array

    def siftDown(self, current_idx, end_idx, heap):
        # Time O(log(n))
        # Space O(1)
        # Write your code here.
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                children_to_swap = child_two_idx
            else:
                children_to_swap = child_one_idx
            if heap[children_to_swap] < heap[current_idx]:
                self.swap(current_idx, children_to_swap, heap)
                current_idx = children_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def siftUp(self, current_idx, heap):
        # Write your code here.
        # Time O(log(n))
        # Space O(1)
        parent_idx = (current_idx - 1) // 2

        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            self.swap(parent_idx, current_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        # Write your code here.
        # Time O(1)
        # Space O(1)
        return self.heap[0]

    def remove(self):
        # Write your code here.
        # Time O(log(n))
        # Space O(1)
        self.swap(0, len(self.heap) - 1, self.heap)

        value_to_remove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    def insert(self, value):
        # Write your code here.
        # Time O(log(n))
        # Space O(1)
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
