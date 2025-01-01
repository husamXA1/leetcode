def maximum_score(s):
    ones = 0
    for c in s:
        if c == "1":
            ones += 1
    
    maximum = 0
    zeros = 0
    for c in s[:-1]:
        if c == "1":
            ones -= 1
        else:
            zeros += 1
        maximum = max(maximum, ones + zeros)
    return maximum
