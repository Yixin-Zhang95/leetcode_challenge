def max_subarray(nums, left, right):
    if left == right:
        return nums[left]
    else:
        p = (left + right) // 2
        max_left = max_subarray(nums, left, p)
        max_right = max_subarray(nums, p+1, right)
        max_cross = max_crossarray(nums, left, p, right)
        return max(max_left, max_right, max_cross)


def max_crossarray(nums, left, p, right):
    if left == right:
        return nums[left]
    cur_left = 0
    cross_l_max = -float('inf')
    for i in range(p, left - 1, -1):
        cur_left += nums[i]
        cross_l_max = max(cur_left,cross_l_max)
    cur_right = 0
    cross_r_max = -float('inf')
    for i in range(p+1, right + 1):
        cur_right += nums[i]
        cross_r_max = max(cur_right, cross_r_max)
    return cross_l_max + cross_r_max


def find(nums):
    print(max_subarray(nums, 0, len(nums) - 1))


find([5,4,-1,7,8])
