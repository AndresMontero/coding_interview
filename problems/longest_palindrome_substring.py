def longestPalindromicSubstring(string):
    # Write your code here.
    # Time O(n^3)
    # Space O(n)
    if string == string[::-1]:
        return string

    longest_palindrome = []

    for i in range(len(string) - 1):
        for j in range(len(string) - 1, -1, -1):
            tmp_string = string[i:j + 1]
            if tmp_string == tmp_string[::-1] and len(tmp_string) > len(longest_palindrome):
                longest_palindrome = tmp_string
    return longest_palindrome


def get_longest_palindrome(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        right += 1
        left -= 1
    return [left + 1, right]


def longestPalindromicSubstring_1(string):
    # Write your code here.
    # Time O(n^2)
    # Space O(1)
    longest = [0, 1]

    for i in range(1, len(string)):
        odd = get_longest_palindrome(string, i - 1, i + 1)
        even = get_longest_palindrome(string, i - 1, i)
        curr_longest = max(odd, even, key=lambda x: x[1] - x[0])
        longest = max(longest, curr_longest, key=lambda x: x[1] - x[0])

    return string[longest[0]: longest[1]]


print(longestPalindromicSubstring("abaxyzzyxf"))
print(longestPalindromicSubstring_1("abaxyzzyxf"))
