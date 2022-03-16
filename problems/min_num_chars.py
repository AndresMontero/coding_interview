def minimumCharactersForWords(words):
    # Write your code here.
    # Time O(n*l) where n is the number of words and l is the length of the lognest word
    # Space O(c) where is c the amount of unique chars
    overall_dict = {}
    for word in words:
        dict_word = {}
        for c in word:
            if c in dict_word:
                dict_word[c] += 1
            else:
                dict_word[c] = 1
        for k, v in dict_word.items():
            if k in overall_dict:
                overall_dict[k] = max(overall_dict[k], v)
            else:
                overall_dict[k] = v

    min_chars = []

    for k, values in overall_dict.items():
        for _ in range(values):
            min_chars.append(k)

    return min_chars


input = ["this", "that", "did", "deed", "them!", "a"]
print(minimumCharactersForWords(input))
