def aux(s, i, wordDict, cache):
    if i >= len(s):
        return True
    if i in cache:
        return cache[i]

    for word in wordDict:
        if word == s[i: i + len(word)]:
            if aux(s, i + len(word), wordDict, cache) == True:
                cache[i] = True
                return True
        else:
            continue
    cache[i] = False
    return False


s = "leetcode"
wordDict = ["leet", "code"]
cache = {}
to_return = aux(s, 0, wordDict, cache)
print(to_return, cache)
