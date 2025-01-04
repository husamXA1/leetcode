# If it works, don't touch it
def countPalindromicSubsequence(self, s: str) -> int:
    counter = 0
    found = set()
    for i in range(len(s)):
        if s[i] in found:
            continue
        found.add(s[i])
        for j in range(len(s) - 1, i, -1):
            if s[i] == s[j]:
                uniqe = set()
                for x in range(i + 1, j):
                    uniqe.add(s[x])
                counter += len(uniqe)
                break
    return counter