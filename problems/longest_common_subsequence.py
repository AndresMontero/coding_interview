def longestCommonSubsequence(str1, str2):
    # Write your code here.
    # Time O(n*m * len(lcs))
    # Space O(n*m * len(lcs))
    matrix = [['' for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    for row in range(1, len(str2) + 1):
        for col in range(1, len(str1) + 1):
            if str2[row - 1] == str1[col - 1]:
                matrix[row][col] = list(matrix[row - 1][col - 1]) + [str2[row - 1]]

            else:
                matrix[row][col] = max(matrix[row - 1][col], matrix[row][col - 1], key=len)

    print(matrix)
    print(matrix[-1][-1])

    return matrix[-1][-1]


print(longestCommonSubsequence("ZXVVYZW", "XKYKZPW"))
