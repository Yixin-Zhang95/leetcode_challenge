import string
def convertToTitle( columnNumber) :
    dic = {}
    for i, n in enumerate(string.ascii_uppercase):
        dic[i] = n
    print(dic)
    result = []
    while columnNumber > 0:
        columnNumber, mod = divmod(columnNumber - 1, 26)
        result.append(dic[mod])
        res = ''
        print(result)
    for i in reversed(range(0, len(result))):
        res = res + result[i]
    return res

print(convertToTitle(29))