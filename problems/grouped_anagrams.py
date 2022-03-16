def groupAnagrams(words):
    # Write your code here.
    # Time O(n^2) where n is the number of words
    # Space O(n*m)  where m is the number of chars in the longest word

    grouped = [0] * len(words)
    anagrams = []
    for i in range(len(words)):
        if grouped[i] == 1:
            continue
        possible_anagram = [words[i]]
        grouped[i] = 1
        chars_dict = {}
        for char in words[i]:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
        for j in range(i, len(words)):
            if len(words[j]) == len(words[i]):
                chars_dict_2 = {}
                for char in words[j]:
                    if char in chars_dict_2:
                        chars_dict_2[char] += 1
                    else:
                        chars_dict_2[char] = 1
                if chars_dict == chars_dict_2 and grouped[j] == 0:
                    grouped[j] = 1
                    possible_anagram.append(words[j])

        if len(possible_anagram):
            anagrams.append(possible_anagram)
    return anagrams


def groupAnagrams_1(words):
    # Write your code here.
    # Time O(n*s*log(s)) where n is the number of word and s is the size of the word
    # Space O(n*s)
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))
print(groupAnagrams_1(words))
