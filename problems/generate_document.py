def generateDocument(characters, document):
    # Write your code here.
    # Time O(n + m) where n and m are the lengths of the characters and document
    # Space O(c ) where c and b are the number of unique letters in characters
    characters_dict = {}

    for c in characters:
        if c not in characters_dict:
            characters_dict[c] = 1
        else:
            characters_dict[c] += 1

    for c in document:
        if c not in characters_dict or characters_dict[c] <= 0:
            return False
        characters_dict[c] -= 1

    return True


if __name__ == '__main__':
    characters = "Bste!hetsi ogEAxpelrt x "
    string = "AlgoExpert is the Best!"
    print(generateDocument(characters, string))
