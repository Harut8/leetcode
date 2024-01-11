from typing import List


def reverseString(self, s: List[str]) -> None:
    lft, rgt = 0, len(s) - 1
    while lft < rgt:
        s[lft], s[rgt] = s[rgt], s[lft]
        lft += 1
        rgt -= 1
    return s
