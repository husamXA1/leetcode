def wordSubsets(words1, words2):
    maxfreq = [0] * 26
    for word in words2:
        freq_word = [0] * 26
        for c in word:
            freq_word[ord(c) - ord('a')] += 1
        for i in range(26):
            maxfreq[i] = max(maxfreq[i], freq_word[i])
    result = []
    for word in words1:
        freq_word = [0] * 26
        for c in word:
            freq_word[ord(c) - ord('a')] += 1
        valid = True    
        for i in range(26):
            if freq_word[i] < maxfreq[i]:
                valid = False
                break
        if valid:
            result.append(word)
    return result

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["l","e"]
print(wordSubsets(words1, words2))