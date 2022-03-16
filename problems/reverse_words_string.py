def reverseWordsInString(string):
    # Write your code here.
    # Time O(n)
    # Space O(n)

    if len(string) <= 1:
        return string

    stack = []
    start_word = 0
    end_word = 0

    for i in range(len(string)):
        if string[i] == ' ':
            end_word = i
            stack.append(string[start_word:end_word])
            start_word = i + 1
            stack.append(' ')
        if end_word != i and i == len(string) - 1:
            stack.append(string[start_word:])

    reversed_words = []
    while len(stack) > 0:
        reversed_words.append(stack.pop())

    return ''.join(reversed_words)


input = "AlgoExpert is the best!"
print(reverseWordsInString(input))
