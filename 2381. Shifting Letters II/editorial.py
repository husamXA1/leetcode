def shiftingLetters(s, shifts):
    diffArray = [0] * len(s)
    for shift in shifts:
        start, end, direction = shift
        if direction == 1:
            diffArray[start] += 1
            if end + 1 < len(s):
                diffArray[end + 1] -= 1
        else:
            diffArray[start] -= 1
            if end + 1 < len(s):
                diffArray[end + 1] += 1
    shiftsCount = 0
    result = ""
    for i in range(len(s)):
        shiftsCount += diffArray[i]
        new_position = (ord(s[i]) - ord('a') + shiftsCount) % 26
        shifted_letter = chr(ord('a') + new_position)
        result += shifted_letter
    return result