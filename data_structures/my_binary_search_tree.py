class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        # left, root, right
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        # left, right, root
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        # root, left, right
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        return sum(self.in_order_traversal())

    def delete_from_max(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_from_max(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_from_max(value)
        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            min_value = self.right.find_min()

            self.data = min_value
            self.right = self.right.delete(min_value)

        return self

    def delete_from_left(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_from_left(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_from_left(value)
        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            max_value = self.left.find_max()
            self.data = max_value
            self.left = self.left.delete_from_left(max_value)

        return self


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [84, 102, 15, 1, 0, 10, 6, 5, 8, 98]
    # numbers = [40, 1, 2, 3, 4, 5, 6, 7, 8]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    # numbers_tree.delete_from_max(84)
    numbers_tree.delete_from_left(84)
    print(numbers_tree.in_order_traversal())
