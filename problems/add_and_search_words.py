class WordDictionary:

    def __init__(self):
        self.root = {}
        self.end_word = '*'

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}

            node = node[c]

        node[self.end_word] = True

    def search(self, word: str) -> bool:

        def dfs(idx, node):  # Do a depth first search iterative
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':  # If char is '.' whe need to look for all the possible combinations in the trie
                    for child in node.values():
                        if type(child) is dict:  # This is important, only call dfs if the child is a node (a dict) ,
                            # otherwise is the end of the trie and should return False
                            if dfs(i + 1, child):
                                return True
                    return False
                else:
                    if c not in node:  # If char is not '.' do the check as in a normal trie, if c not in dict return false
                        return False

                    node = node[c]

            return self.end_word in node

        root = self.root
        result = dfs(0, root)

        return result
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)