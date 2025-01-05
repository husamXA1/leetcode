# Time Limit Exceeded
def shiftingLetters(s, shifts):
    shiftValues = [0] * len(s)
    for shift in shifts:
        value = -1 if shift[2] == 0 else 1
        for i in range(shift[0], shift[1] + 1):
            shiftValues[i] += value
    result = ""
    for i in range(len(s)):
        new_position = (ord(s[i]) - ord('a') + shiftValues[i]) % 26
        shifted_letter = chr(ord('a') + new_position)
        result += shifted_letter
    return result