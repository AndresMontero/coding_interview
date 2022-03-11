def levenshteinDistance(str1, str2):
    # Write your code here.
    # Time O(n * m)
    # Space O(n * m)
    matrix = [[x for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]

    for j in range(1, len(str1) + 1):
        matrix[j][0] += j

    for r in range(1, len(str1) + 1):
        for c in range(1, len(str2) + 1):
            if str1[r - 1] == str2[c - 1]:
                matrix[r][c] = matrix[r - 1][c - 1]
            else:
                matrix[r][c] = 1 + min(matrix[r][c - 1], matrix[r - 1][c], matrix[r - 1][c - 1])

    return matrix[-1][-1]

if __name__ == '__main__':
    str1 = "abc"
    str2 = "yabd"

    print(levenshteinDistance(str1, str2))