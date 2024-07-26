# https://leetcode.com/problems/two-sum/
nums = [2, 7, 11, 15]
target = 9


def two_sum(nums, target):
    _res_dct = dict()
    for i, j in enumerate(nums):
        _rem = target - j
        if _rem in _res_dct:
            return [_res_dct[_rem], i]
        else:
            _res_dct[j] = i
    return _res_dct


print(two_sum(nums, target))
