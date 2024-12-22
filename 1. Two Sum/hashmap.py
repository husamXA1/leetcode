def two_sum(arr, target):
    compliments = {}
    for i in range(len(arr)):
        if arr[i] in compliments:
            return [compliments[arr[i]], i]
        compliment = abs(target - arr[i])
        compliments[compliment] = i
    return [-1, -1]

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))

nums = [3, 3]
target = 6
print(two_sum(nums, target))
