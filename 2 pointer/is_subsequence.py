# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    s_i = 0
    t_i = 0
    while t_i < len(t):
        if s[s_i] == t[t_i]:
            s_i += 1
        if s_i == len(s):
            return True
        t_i += 1
    return False

print(isSubsequence("abc", "ahbgdc"))