# https://leetcode.com/problems/valid-palindrome/

s = "A man, a plan, a canal: Panama"


def is_palindrome(s: str) -> bool:
    lft, rgt = 0, len(s) - 1
    while lft < rgt:
        while lft < rgt and not s[lft].isalnum():
            lft += 1
        while lft < rgt and not s[rgt].isalnum():
            rgt -= 1
        if s[lft].lower() != s[rgt].lower():
            return False
        lft += 1
        rgt -= 1
    return True


print(is_palindrome('.,'))
