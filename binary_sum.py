def addBinary(a, b) :
    carry = 0
    ans = []
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)
    for i in range(n-1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1
        if carry % 2 == 1:
            ans.append('1')
        else:
            ans.append('0')
        if carry < 2:
            carry = 0
        else:
            carry = 1
    if carry == 1:
        ans.append('1')
    ans.reverse()
    return ''.join(ans)


a = '01'
b = '10'
print(addBinary(a, b))