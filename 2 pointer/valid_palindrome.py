# https://leetcode.com/problems/valid-palindrome/
### FULLY DONE ###
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
"""
XNDRIN KARELI E MOTENAL 2 POINTER I MIJOCOV
VERCNEQ 2 KET LEFT, RIGHT  (0, len(s) - 1)
MIAJAMANAK 2 KOXMIC NAYELOV GANQ EV BAC TOXNENQ AYN SYMBOLNERY
VORONQ VOR ALPHABETICAL KAM NUMERICAL CHEN
AYD AMENY ANUM ENQ AYNQAN JAMANAK QANI DER
2 POINTERNERY CHEN HATVEL IRAR HET EV MER NAYAC SYMBOLNERY IRAR HAVASAR CHEN

AYSINQN PTTVUM ENQ CYCLE QANI DER LFT<RGT
BAC ENQ TOXNUM BOLOR VOCH ALPHA EV NUM SYMBOLNERY
EV ETE KA GONE MEK HAT VOCH HAVAR SYMBOL AJIC EV DZAXIC UREMN FALSE 'ABCA' B!=C 
"""