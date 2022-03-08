def firstNonRepeatingCharacter(string):
    # Write your code here.
    # O(n) time where n is the len of the string
    # O(c) space, c is the number of unique characters
    characters_dict = {}
    for c in string:
        if c not in characters_dict:
            characters_dict[c] = 1
        else:
            characters_dict[c] += 1

    for i in range(len(string)):
        if characters_dict[string[i]] == 1:
            return i

    return -1


if __name__ == '__main__':
    print(firstNonRepeatingCharacter("abcdcaf"))
