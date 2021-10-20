def minMoves(nums) -> int:
    min_num = 0
    max_num = 0
    count = 0
    while True:
        for i in range(0, len(nums)):
            if nums[i] < nums[min_num]:
                min_num = i
        for i in range(0, len(nums)):
            if nums[i] > nums[max_num]:
                max_num = i
        diff = nums[max_num] - nums[min_num]
        if diff == 0:
            break
        else:
            count += diff
            for i in range(0, len(nums)):
                if i != max_num:
                    nums[i] += diff
    return count


print(minMoves([1,2,3]))