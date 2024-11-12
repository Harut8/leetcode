# https://leetcode.com/problems/longest-palindromic-substring

def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)
        longest = max(longest, palindrome1, palindrome2, key=len)

    return longest

"""
PALINDROME STANALIS KAROX ENQ UNENAL 2 CASE
ERB TOGHY UNI KENT KAM EL ZUYG ERKARUTYUN
===============
Если строка — "abc", то каждый символ "a", "b", "c" может быть "центром" потенциального палиндрома.
Итак, у нас есть 𝑛
n таких центров, по одному для каждого символа:
Центр над символом 0.
Центр над символом 1.
Центр над символом 2, и так далее до символа n - 1.
===============
Если строка имеет 𝑛
n символов, то между каждым соседними символами у нас есть 𝑛−1
n−1 таких промежутков, на которых могут быть палиндромы четной длины:
Промежуток между символом 0 и 1.
Промежуток между символом 1 и 2.
Промежуток между символом 2 и 3, и так далее до промежутка между символами n - 2 и n - 1.
===============
CENTER = 2*n - 1
"""