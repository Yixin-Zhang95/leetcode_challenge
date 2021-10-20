def Palindrome(s):
#     s_filtered = filter(lambda s: s.isalnum(), s)
#     s_lowercase = map(lambda s: s.lower(), s_filtered)
#     s_forward = list(s_lowercase)
#     s_backward = s_forward[::-1]
#     return s_forward == s_backward
#
# print(Palindrome("A man, a plan, a canal: Panama"))
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


print(Palindrome("A man, a plan, a canal: Panama"))