# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.min_max_list = [] # list of tuples [(min, max)]
        self.stack = []

    def peek(self):
        # Write your code here.
        if len(self.min_max_list) < 1:
            return []

        return self.stack[-1]

    def pop(self):
        # Write your code here.
        if len(self.min_max_list) < 1:
            return []

        self.min_max_list.pop()
        return self.stack.pop()

    def push(self, number):
        # Write your code here.
        if len(self.min_max_list) < 1:
            self.min_max_list.append((number, number))
        else:
            current_min = self.min_max_list[-1][0]
            current_max = self.min_max_list[-1][1]
            self.min_max_list.append((min(current_min, number), max(current_max, number)))

        self.stack.append(number)

    def getMin(self):
        # Write your code here.
        if len(self.min_max_list) < 1:
            return []

        current_min = self.min_max_list[-1][0]
        return current_min

    def getMax(self):
        # Write your code here.
        if len(self.min_max_list) < 1:
            return []

        current_max = self.min_max_list[-1][1]
        return current_max
