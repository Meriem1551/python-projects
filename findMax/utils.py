def findMax(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max
