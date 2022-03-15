def balancedBrackets(string):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    match_dict = {')': '(', ']': '[', '}': '{'}
    open_chars = ['(', '{', '[']
    close_chars = [')', '}', ']']
    my_stack = []

    for char in string:
        if char in open_chars:
            my_stack.append(char)

        elif char in close_chars:
            if len(my_stack) < 1:
                return False
            else:
                last_value_in_stack = my_stack.pop()
                if last_value_in_stack != match_dict[char]:
                    return False

    if len(my_stack):
        return False
    else:
        return True


print(balancedBrackets("([])(){}(())()()"))