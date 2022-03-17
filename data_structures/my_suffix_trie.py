# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        # Time O(n^2)
        # Space O(n^2)
        for i in range(len(string)):
            self.insert_substring_starting_at(i, string)

    def insert_substring_starting_at(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

        node[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        # Time O(m) where m is the lenght of the string to search
        # Space O(1)
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node


trie = SuffixTrie("babc")
print(trie)