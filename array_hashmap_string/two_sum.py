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

def two_sum2(nums, target):
    nums.sort()
    start, end = 0, len(nums) - 1
    while start < end:
        _sum = nums[start] + nums[end]
        if _sum == target:
            return [start, end]
        elif _sum < target:
            start += 1
        else:
            end -= 1
    return None


print(two_sum(nums, target))
print(two_sum2(nums, target))
