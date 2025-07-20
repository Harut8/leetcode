s = "anagram"
t = "nagaram"


def isAnagram(s, t):
    """
    Time Complexity: O(nlogn) - sorting both strings
    Space Complexity: O(n) - storing sorted strings
    """
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

def isAnagram2(s, t):
    """
    Time Complexity: O(n) - single pass through both strings
    Space Complexity: O(k) - where k is size of character set (26 for lowercase letters)
    """
    _len_s = len(s)
    _len_t = len(t)
    if _len_s != _len_t:
        return False
    _counter_s = {}
    _counter_t = {}
    for i in range(_len_s):
        _counter_s[s[i]] = _counter_s.get(s[i], 0) + 1
        _counter_t[t[i]] = _counter_t.get(t[i], 0) + 1
    return _counter_s == _counter_t

print(isAnagram(s, t))
print(isAnagram2(s, t))
