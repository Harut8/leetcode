# https://leetcode.com/problems/group-anagrams/
import collections


def group_anagrams(strs):
    _answers = collections.defaultdict(list)
    for _str in strs:
        _key = "".join(sorted(_str))
        _answers[_key].append(_str)
    return list(_answers.values())
