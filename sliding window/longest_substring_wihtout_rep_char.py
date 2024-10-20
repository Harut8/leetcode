# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def longest_substring(s):
    left = 0
    max_sub = 0
    chars = set()
    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[r])
        max_sub = max(max_sub, r - left + 1)
    return max_sub
s = "abcabcbb"
print(longest_substring(s))

"""
VERCNENQ 2 POINTER LEFT, RIGHT 0, 0
VORPESZI HASKANANQ REPEATINGI PAHY MEZ PETQ E NAYEV SET
EV AMEN LELEMENTI HAMAMR MENQ KAROX ENQ DYNCKIC HASHVEL 
MAXIMAL SUBSTRING Y YNDUNELOV SKZBIC AYN HAVASAR 0 I
EV HASNELOV AYN KETIN ERB SKSVUM E KRKNVEL ORINAK "ABCA" I
MEJ "ABC" N OKA BAYC SKSAC 2 RD A IC PETQ E MAQREL SET Y EV LEFT Y SHRINK ANEL
U AMEN ELEMENTI HAMAR MAX HASHVENQ 
"""