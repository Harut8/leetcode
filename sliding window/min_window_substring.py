# https://leetcode.com/problems/minimum-window-substring/


from collections import defaultdict, Counter


def min_window(s, t):
    t_counter = Counter(t)
    current_counter = defaultdict(int)
    required = len(t_counter)
    left = 0
    formed = 0
    min_len = float('inf')
    result = ""

    for r in range(len(s)):
        current_counter[s[r]] += 1
        if s[r] in t and current_counter[s[r]] == t_counter[s[r]]:
            formed +=1
        while left < r and formed == required:
            chr = s[left]
            if r - left + 1 < min_len:
                min_len = r - left + 1
                result = s[left:r+1]
            current_counter[chr] -= 1
            if chr in t and current_counter[chr] < t_counter[chr]:
                formed -=1
            left += 1
    return result

s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))

"""
QANI VOR MENQ PETQ E GTNENQ SUBSTRING
KAROX ENQ OGTVEL SLIDING WINDOW I EV 2 POINTER I GAXAPARIC
SKZBI HAMAR ASENQ VOR LUCUM ENQ HAMARYA ANNAGRAMI XNDIR
AYSINQN MEZ PETQ E DICT VORI MEJ KUNENANQ T I BOLOR SYMBOLNERI QANAKY
EV CURRENT WINDOW I ELEMENTNERI QANAKY
MITQY KAYANUM E NRANUM VOR SKZBI HAMAMR UXXAKI GTNENQ INCH VOR SUBSTRING
VORY KPARUNAKI T I BOLOR ELEMENTNERY IR QANAKUTYAMN NOR MTACENQ MINIMUM I MASIN
AYSINQN VERCNENQ LEFT, RIGHT HETO MECACNENQ AYNQAN QANI DER CHENQ LUCEL
EV HETO OPTIMIZACNENQ LEFT I ELEMENTNERY JNJELOV
EV NAYEV NSHENQ VOR ANNAGRAMI XNDIRY LUCVAC KLINI ETE 
ELEMENTY GTNVI T I MIJIC EV COUNTERI  ARJEQY AYD ELEMENTI HAMAR LINI
NUYN I INCH T UM=> AYD JAMANAK KAROX ENQ HAMAREL VOR 1 SYMBOLI HAMAMR XNDIRY LUCVEC
EV AMBOXJ XNDIRY KLUCVI ETE T I BOLOR SYMOLNERI HAMAR GTNENQ AYDPISIN
EV PAHENQ MIN_LEN VOR AMEN ANGAM EVLI POQR CHAPI WINDOW GTNELIS UPDATE ANENQ
EV DNENQ NOR RESULT
"""