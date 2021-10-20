def addStrings(num1, num2) -> str:
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    residue = 0
    output = []
    while p1 >= 0 or p2 >= 0:
        if p1 >= 0:
            x1 = ord(num1[p1]) - ord('0')
        else:
            x1 = 0
        if p2 >= 0:
            x2 = ord(num2[p2]) - ord('0')
        else:
            x2 = 0
        print('x1',x1)
        print('x2',x2)
        result = (x1 + x2 + residue) % 10
        print('result',result)
        residue = (x1 + x2 + residue) // 10
        print('residue',residue)
        output.append(result)
        p1 -= 1
        p2 -= 1
        print('output',output)
    output.append(residue)
    print('output', output)

    reversed_output = output[::-1]
    # str_output = [str(x) for x in reversed_output]
    str_output = []
    for x in reversed_output:
        str_output.append(str(x))
    return ''.join(str_output)



print(addStrings('9','99'))