function waysToSplitArray(nums) {
    let rightSum = 0
    for (num of nums) rightSum += num
    let counter = 0
    let leftSum = 0
    for (let i = 0; i < nums.length - 1; i++) {
        leftSum += nums[i]
        rightSum -= nums[i]
        if (leftSum >= rightSum) counter++ 
    }
    return counter
}
