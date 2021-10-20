def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    count = 0
    for i range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[j] - arr[i]) <= a:
                for k in range(j + 1, len(arr)):
                    if abs(arr[j] - arr[k]) <= b & abs(arr[i] - arr[k]) <= c:
                        count += 1

    return count

