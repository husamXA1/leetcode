def is_palindrome(num):
    num = str(num)
    for i in range(len(num) // 2):
        if num[i] != num[-i - 1]:
            return False
    return True

test_cases = [121, -121, 10, 321, 12321]
for case in test_cases:
    print(is_palindrome(case))
