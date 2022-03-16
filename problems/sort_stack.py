def aux_insert(current_top, stack):
    if len(stack) < 1:
        stack.append(current_top)
        return
    else:
        if stack[-1] <= current_top:
            stack.append(current_top)
            return
        else:
            tmp = stack.pop()
            aux_insert(current_top, stack)
            stack.append(tmp)


def sortStack(stack):
    # Write your code here.
    # Time O(n^2)
    # Space O(n)
    if len(stack) < 1:
        return stack

    current_top = stack.pop()
    sortStack(stack)
    aux_insert(current_top, stack)

    return stack


input = [-5, 2, -2, 4, 3, 1]
print(sortStack(input))
