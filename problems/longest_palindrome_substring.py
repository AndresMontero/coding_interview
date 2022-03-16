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


print(longestPalindromicSubstring("abaxyzzyxf"))
