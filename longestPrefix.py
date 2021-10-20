def longestPrefix(s):
    if len(s) == 0:
        return ''
    Prefix = ''
    for i in range(len(min(s))):
        ref = s[0][i]
        if all(character[i] == ref for character in s):
            Prefix += ref
        else:
            break
    return Prefix


s = ["flower","flow","flight"]
print(longestPrefix(s))
