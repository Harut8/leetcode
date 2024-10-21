# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/

def maxVowels(s, k):
    vowels = set("aeiou")
    window_counter = 0
    max_vowels = 0
    i = 0
    while i < len(s):
        if s[i] in vowels:
            window_counter += 1
        if i >= k and s[i - k] in vowels:
            window_counter -= 1
        max_vowels = max(max_vowels, window_counter)
        i += 1
    return max_vowels

s = "abciiidef"
k = 3

print(maxVowels(s, k))
"""
MEZ PETQ E SLIDING WINDOW
VORY AMEN QAYLI JAMANAK ETE ELEMENTY VOWELI MEJICA + 1 KANI QANAKY
AYSINQN CURRENT WINDOW I MEJ GTNVOX VOWELS I QANAKY
KLINI KET VORTEXIC SKSAC WINDOW I CHAPIC DURS VOWELNER PETQ -1 ANENQ
AYD KETN E I>=K APA S[I-K] RD  ELEMENETY DURS E WINDOW IC AYSINQN -1
EV ETE WINDOW CHAPOV ELEMENTI VRAYOV GNACEL ENQ KAROX ENQ SKSEL MAX HASHVEL
"""