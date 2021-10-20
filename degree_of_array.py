def firstBadVersion(n):
    left = 1
    right = n
    while left <= right:
        mid = (right + left) // 2
        if firstBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left
#         return min_degree

nums = [1,2,2,3,1,4,2]
print(findShortestSubArray(nums))