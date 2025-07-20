# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        _rans = Counter(ransomNote)
        _mag = Counter(magazine)
        for k, v in _rans.items():
            if _mag.get(k, 0) < v:
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))