from collections import deque
from unicodedata import name


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(text):
    stack = Stack()
    for c in text:
        stack.push(c)
    result = ''
    while not stack.is_empty():
        result += stack.pop()

    return result


def is_balanced(text):
    """
        Function to determine if a sequence of parenthesis is balanced or not
    :param text:
    :return:
    """
    stack = Stack()
    mapping = {")": "(", "}": "{", "]": "["}

    for c in text:
        if c == '(' or c == '[' or c == '{':
            stack.push(c)
        if c == ')' or c == ']' or c == '}':
            if stack.is_empty():
                return False
            else:
                if mapping[c] != stack.pop():
                    return False

    if stack.is_empty():
        return True
    else:
        return False


def main():
    original_text = "We will conquere COVID-19"
    reversed_text = reverse_string(original_text)
    print(f'The original text is: {original_text}, \nThe reversed text is {reversed_text}')

    sequences_to_test = ["({a+b})", "))((a+b}{", "((a+b))", "))", ")(", '[a+b]*(x+2y)*{gg+kk}']
    print('***************')
    for sequence in sequences_to_test:
        if is_balanced(sequence):
            print(f'The sequence {sequence} is balanced ')
        else:
            print(f'The sequence {sequence} is not balanced ')


if __name__ == '__main__':
    main()
