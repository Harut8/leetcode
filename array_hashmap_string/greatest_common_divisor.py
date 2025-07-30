# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75


from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        If str1 and str2 are composed of the same substring, then the GCD of
        the two lengths should be the length of the repeated substring.
        EXAMPLE:
        str1 = "ABCABC", str2 = "ABC"
        len(str1) = 6, len(str2) = 3
        gcd(len(str1), len(str2)) = 3

        str1 = "ABABAB", str2 = "ABAB"
        len(str1) = 6, len(str2) = 4
        gcd(len(str1), len(str2)) = 2

        str1 = "LEET", str2 = "CODE"
        len(str1) = 4, len(str2) = 4
        gcd(len(str1), len(str2)) = 1
        """
        if str1 + str2 != str2 + str1:
            return ""

        gc = gcd(len(str1), len(str2))
        return str2[:gc]