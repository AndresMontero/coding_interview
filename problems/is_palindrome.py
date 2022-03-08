def isPalindrome_3(string):
    # Write your code here.
    # Time O(n)
    # Space O(1)
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


def aux(string, start, end):
    if start >= end:
        return True
    if string[start] == string[end]:
        return aux(string, start + 1, end - 1)
    else:
        return False


def isPalindrome_2(string):
    # Write your code here.
    # Time O(n)
    # Space O(l) where l is how long the palindrome is

    return aux(string, 0, len(string) - 1)


def isPalindrome(string):
    # Write your code here.
    # Time O(n)
    # Space O(n)
    if string == string[-1::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isPalindrome("abcdcba"))
    print(isPalindrome_2("abcdcba"))
    print(isPalindrome_3("abcdcba"))
