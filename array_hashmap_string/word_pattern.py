# https://leetcode.com/problems/word-pattern/submissions/1704498827/?envType=study-plan-v2&envId=top-interview-150

def wordPattern(pattern: str, s: str) -> bool:
    _words = s.split(' ')
    if len(_words) != len(pattern):
        return False
    _symbol_to_word = {}
    _word_to_symbol = {}
    for i, j in zip(pattern, _words):
        if i in _symbol_to_word and _symbol_to_word[i] != j:
            return False
        if j in _word_to_symbol and _word_to_symbol[j] != i:
            return False
        _symbol_to_word[i] = j
        _word_to_symbol[j] = i
    return True

print(wordPattern("abba", "dog cat cat dog"))