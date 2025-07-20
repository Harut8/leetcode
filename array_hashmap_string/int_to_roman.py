# https://leetcode.com/problems/roman-to-integer/submissions/


def romanToInt(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]
    return result
"""
MENQ PET Q HASHVI ARNENQ AYN PASTY 
VOR ETE HAJORDOX SYMBOL Y AVELI MEC ARJEQ E PARUNAKUM QAN NAXORDOXY
ORINAK IV DA NSHANAKUM E VOR TOTAL IC PETQ E HANENQ AYS ELEMENTI CHAPOV
HARAK DEPQUM GUMARENQ 
ORINAK
TOTAL = 0
0 RD ELEMENTY 1 EV HAJORD Y AYSINQN 5 MEC E IRANIC DRA HAMAR HANUM ENQ TOTAL=-1
1 RD Y GUMARUM
"""