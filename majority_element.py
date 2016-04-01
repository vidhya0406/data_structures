def majorityElement(nums):
    count = 0
    key = None
    for i in range(0, len(nums)):
        if count == 0:
            key = nums[i]
            count = 1
        else:
            if key == nums[i]:
                count += 1
            else:
                count -= 1
    return key

print(str(majorityElement(['a','a', 'a', 'b'])))
