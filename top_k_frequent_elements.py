# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter

nums = [1, 1, 1, 2, 2, 3]
k = 2


def _counter_elements(nums):
    _counter = {}
    for _num in nums:
        _counter[_num] = _counter.get(_num, 0) + 1
    return _counter


def solution(_nums):
    _nums = Counter(_nums).most_common()
    return [i[0] for i in _nums[:k]]


def via_heap(_nums):
    _counter = {}
    for _num in _nums:
        _counter[_num] = _counter.get(_num, 0) + 1
    import heapq
    return heapq.nlargest(k, _counter.keys(), key=_counter.get)
