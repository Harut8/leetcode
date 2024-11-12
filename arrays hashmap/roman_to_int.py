# https://leetcode.com/problems/integer-to-roman/submissions/

class Solution(object):
    def intToRoman(self, num):
        int_roman_values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        res = []
        for val, symb in int_roman_values:
            while num >= val:
                num -= val
                res.append(symb)
        return "".join(res)


"""
PAHUM ENQ NVAZMAN KARGOV TVERY
HETO ITERATE LINUM EV QANI DER NUM Y MEC E VAL IC 
AYSINQN DER CHENKQ KAROX ANCNEL AVELI POQR TVI SHARUNAKUM ENQ HANEL DRANIC
"""