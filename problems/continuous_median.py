class min_heap:
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


class max_heap:
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
            if child_two_idx != -1 and heap[child_two_idx] > heap[child_one_idx]:
                children_to_swap = child_two_idx
            else:
                children_to_swap = child_one_idx
            if heap[children_to_swap] > heap[current_idx]:
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

        while current_idx > 0 and heap[current_idx] > heap[parent_idx]:
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


# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.lower_half = max_heap([])
        self.upper_half = min_heap([])

    def rebalance_heaps(self):
        if len(self.lower_half.heap) > len(self.upper_half.heap):
            tmp = self.lower_half.remove()
            self.upper_half.insert(tmp)
        else:
            tmp = self.upper_half.remove()
            self.lower_half.insert(tmp)

    def insert(self, number):
        # Write your code here.
        # Time O(log(n))
        # Space O(n)
        if len(self.lower_half.heap) == 0:
            self.lower_half.insert(number)

        else:
            if number > self.lower_half.peek():
                self.upper_half.insert(number)

            else:
                self.lower_half.insert(number)

        if abs(len(self.lower_half.heap) - len(self.upper_half.heap)) > 1:
            self.rebalance_heaps()

        if len(self.lower_half.heap) == len(self.upper_half.heap):
            self.median = (self.lower_half.peek() + self.upper_half.peek()) / 2

        else:
            self.median = self.lower_half.peek() if len(self.lower_half.heap) > len(self.upper_half.heap) \
                else self.upper_half.peek()

        # print(self.lower_half.heap)
        # print(self.upper_half.heap)

    def getMedian(self):
        return self.median


handler = ContinuousMedianHandler()
handler.insert(5)
handler.insert(10)
print(handler.getMedian())
handler.insert(100)
print(handler.getMedian())
