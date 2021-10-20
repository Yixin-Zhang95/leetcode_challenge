def reverse(x):
    if x > 0:
        flag = 1
    else:
        flag = -1
    x = str(abs(x))
    r_x = int(x[::-1])
    if r_x <= 2**31 -1:
        return r_x * flag
    else:
        return 0


print(reverse(1534236469))