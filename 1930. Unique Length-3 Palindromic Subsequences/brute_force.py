# Time Limit Exceeded
def countPalindromicSubsequence(self, s: str) -> int:
    subsequences = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                if s[i] == s[k]:
                    subsequences.add(s[i] + s[j] + s[k])
    return len(subsequences)