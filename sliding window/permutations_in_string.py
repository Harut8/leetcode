# https://leetcode.com/problems/permutation-in-string/
import collections


def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    s1_count = collections.Counter(s1)
    s2_count = collections.defaultdict(int)
    for i in range(len(s2)):
        s2_count[s2[i]] += 1
        if i - len(s1) >= 0:
            s2_count[s2[i - len(s1)]] -= 1
            if s2_count[s2[i - len(s1)]] == 0:
                del s2_count[s2[i - len(s1)]]
        if s1_count == s2_count:
            return True
    return False
print(checkInclusion("ab", "eidbaooo"))

"""
UNENQ S1 EV S2
QANI VOR S1 Y PETQ E LINI S2 I MEJ APA LEN(S1) < LEN(S2)
MENQ PETQ E SKSENQ TRUE KAM FALSE NAYEL MIAYN SKSAC LEN(S1) I CHAP ELEMENT NAYELUC HETO
AYSINQN ERB I - LEN(S1) >= 0 KAM NUYNN E VOR I >= LEN(S1)
MIEVNUYN JAMANAK MENQ PETQ E GUMARENQ WINDOW I MEJ GTNVOX ELEMENTNERI QANAKY AMEN ETAPUM
EV ETE SKSEC BAVARAREL S1 I CHAPIC AVEL ELEMENTNERI PAYMANIN
PETQ E ELEMENTNERI QANAKUTYAN MEJ CHTOXNENQ AVELORD ELEMENTNER AYSINQN
WINDOW I CHAPIC DURS GTNVOX ELEMENTNERY ORINAK "EIDB" I DEPQUM
ERB SKSENQ NAYEL KLINI E: 1 I: 1 ARAJIN 2 QAYLEROV
SKSAC D IC MENQ KUNENANQ VOR E N DURS E MNUM WINDOW IC 
AYSINQN PETQ E HANENQ 1 EV ETE CHMNAC JNJENQ
WINDOW IC DURS EN CANKACAC I - LEN(S1) ELEMENT
"""