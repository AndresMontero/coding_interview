# Time O(2^n) | Space O(2^n)


def back_track(open_count, close_count, stack, res):
    if open_count == close_count == 0:
        res.append("".join(stack))
        return

    if open_count > 0:
        stack.append("(")
        back_track(open_count - 1, close_count, stack, res)
        stack.pop()

    if close_count > open_count:
        stack.append(")")
        back_track(open_count, close_count - 1, stack, res)
        stack.pop()


stack = []
res = []
back_track(3, 3, stack, res)
print(res)
