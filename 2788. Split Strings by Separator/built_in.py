def split_strings(words, separator):
    result = []
    for word in words:
        result.extend(word.split(separator))
    while "" in result:
        result.remove("")
    return result

words = ["one.two.three", "four.five", "six"]
separator = "."

print(split_strings(words, separator))
