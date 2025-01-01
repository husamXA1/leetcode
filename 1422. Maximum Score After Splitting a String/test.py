from two_pointers import maximum_score

test_cases = [
    "011101",
    "00111",
    "1111",
    "00"
]

expected_output = [5, 5, 3, 1]

for i in range(len(expected_output)):
    if maximum_score(test_cases[i]) == expected_output[i]:
        print(f"Test case {i}: passed")
        print(f"input: {test_cases[i]}, output: {expected_output[i]}")
    else:
        print(f"Test case {i}: failed")
        print(f"input: {test_cases[i]}, output: {maximum_score(test_cases[i])}")
