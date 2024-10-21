# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import defaultdict


# def longest_repeating_char(s, k):
#     left = 0
#     char_freq = defaultdict(int)
#     max_freq = max_len = 0
#     for right in range(len(s)):
#         char_freq[s[right]] += 1
#         window_size = right - left + 1
#         max_freq = max(max_freq, char_freq[s[right]])
#         while window_size - max_freq > k:
#             left += 1
#             char_freq[s[left]] -= 1
#         max_len = max(max_len, right - left + 1)
#     return max_len

def longest_repeating_char(s, k):
    max_len = 0
    window_char_freq = defaultdict(int)
    max_freq = 0
    l = 0
    for r in range(len(s)):
        window_char_freq[s[r]] += 1
        max_freq = max(max_freq, window_char_freq[s[r]])
        if r - l + 1 - max_freq > k:
            window_char_freq[s[l]] -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

s = "ABAB"
k = 2
print(longest_repeating_char(s, k))

"""
XNDRI MITQY KAYANUM E NRANUM VOR MENQ IMANANQ
AMENASHAT HANDIPOX ELEMENTY MER WINDOW I MEJ
AYSINQN ETE UNENQ "ABC" MEZ HAMAMR KAREVOR CHE TE
VOR ELEMENTN E AMENASHATY HANDIPUM AYL TIVN E KAREVOR
QANI VOR ETE KA "ABC" AYSINQN MAX_FREQ_EL = 1
UREMN UNENQ EVS 2 ELEMENT VORONQ VOR IRARIC TARBER EN
DA KAROX ENQ HASKANANL HETEVYAL KERP
WINDOW SIZE = RIGHT - LEFT + 1
POPOXVOV ELEMENTNERI QANAKY WINDOW_SIZE - MAX_FREQ_EL
AYSINQN "ABC" I DEPQUM WINDOW = 3
BAYC MAX_FREQ_EL = 1 AYSINQN KA EVS 2 ELEMENT POPOXELU KARIQ
ETE WINDOW_SIZE - MAX_FREQ_EL >= K SA NSHANAKUM E VOR SXAL UXXUTYAN VRA ENQ
PETQ E NEXACNEL WINDOW I CHAPY QANI DER AYS PAYMANY CHI BAVARARVUM
EV AMEN ETAPI JMNK VERAHASHVARK ANEL MAX_FREQ Y INCHPES NAYEV LEN Y
"""