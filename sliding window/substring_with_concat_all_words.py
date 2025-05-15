# https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter


def findSubstring(s: str, words: list[str]) -> list[int]:
    if len(words) == 0:
        return []
    word_len = len(words[0])
    word_count = len(words)
    total_count = word_len * word_count
    word_counter = Counter(words)
    res = []
    for i in range(0, len(s) - total_count+1):
        substring = s[i: i + total_count]
        perm = [
            substring[j: j + word_len] for j in range(0, total_count, word_len)
        ]
        if Counter(perm) == word_counter:
            res.append(i)
    return res



s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))


"""
AYSTEX KA HETAQRQIR PAYMAN VOR 
AMEN BAR WORDS I MEJ UNI NUYN ERKARUTYUNY MENQ DRANIC KAROX ENQ OGTVEL
EV GTNEL MEZ PETQ EKOX SUBSTRINGNER I CHAPY AYSINQN
LEN(WORDS) * LEN(WORDS[O)) KLINI MER SUBSTRING I CHAPY AMEN QAYLI HAMAR
ORINAK barfoo, arfoot, rfooth, ...
EV AMEN AYSPISI SUBSTRING Y PET Q BAJANENQ WORD I CHAPANI MASERI
AYSIQNN SUBSTRING[J:J + LEN(WORDS[O))] SKSAC 0 IC MINCHEV TOTAL_WORD I CHAP AMEN QAYLI MECACNELOV
WORD I CHAPOV
ORINAK barfoo I HAMAR KUNENANQ
SUBSTRING[0:3] EV SUBSTRING[3:6] VORY NUYNN E INCH
FOR J IN RANGE(0, TOTAL_WORD, LEN(WORDS[O]))
"""