# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


def two_sum(nums, target):
    _slow, _fast = 0, len(nums) - 1
    while _slow < _fast:
        _sum = nums[_slow] + nums[_fast]
        if _sum == target:
            return [_slow + 1, _fast + 1]
        elif _sum < target:
            _slow += 1
        else:
            _fast -= 1
    return [-1, -1]


print(two_sum([2, 7, 11, 15], 9))
