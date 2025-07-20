# https://neetcode.io/problems/string-encode-and-decode?list=neetcode150


def encode(s: list[str]) -> str:
    _temp = []
    for el in s:
        _l = len(el)
        _temp.append(f"{_l}:{el}") # : needed to handle cases when str length > 9
    return "".join(_temp)

def decode(s: str) -> list[str]:
    _temp = []
    i = 0
    while i < len(s):
        _l = 0
        while i < len(s) and s[i] != ":": # when str length < 9 without this will work fine
            _l = _l * 10 + int(s[i])
            i += 1
        i += 1
        _temp.append(s[i:i + _l])
        i += _l
    return _temp


s = ["hello", "world"]
print(encode(s))
print(decode(encode(s)))