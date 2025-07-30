# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        vowels = set('aeiouAEIOU')
        pos = [i for i, ch in enumerate(l) if ch in vowels]
        i, j = 0, len(pos) - 1
        while i < j:
            l[pos[i]], l[pos[j]] = l[pos[j]], l[pos[i]]
            i += 1
            j -= 1
        return "".join(l)
