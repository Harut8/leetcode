# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    _char_map = {}
    for i in range(len(s)):
        if s[i] not in _char_map:
            _char_map[s[i]] = t[i]
        elif _char_map[s[i]] != t[i]:
            return False
    return True

def isIsomorphic2(s: str, t: str) -> bool:
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))