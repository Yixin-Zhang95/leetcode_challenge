def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    revernum = 0
    while x > revernum:
        revernum = x % 10 + revernum * 10
        x = x // 10
        print('revernum', revernum)
        print('x', x)
    return x == revernum or x == revernum // 10


print(isPalindrome(121))
