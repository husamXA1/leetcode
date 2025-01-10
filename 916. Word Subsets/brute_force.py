# Time limit exceeded
def wordSubsets(words1, words2):
    result = []
    for a in words1:
        valid = True
        for b in words2:
            if not isSubset(a, b):
                valid = False
                break
        if valid:
            result.append(a)
    return result

def isSubset(a, b):
    freqb = {}
    for c in b:
        freqb[c] = freqb.get(c, 0) + 1
    freqa = {}
    for c in a:
        freqa[c] = freqa.get(c, 0) + 1
    for key in freqb:
        if key not in freqa or freqa[key] < freqb[key]:
            return False
    return True

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["l","e"]
print(wordSubsets(words1, words2))