def minOperations(boxes):
    result = []
    for i in range(len(boxes)):
        counter = 0
        for j in range(len(boxes)):
            if i == j or boxes[j] == "0":
                continue
            counter += abs(i - j)
        result.append(counter)
    return result