# https://leetcode.com/problems/contains-duplicate/

def contains_duplicate(nums):
    return len(nums) != len(set(nums))


def contains_duplicate_2(nums):
    _hash_map = dict()
    for i in nums:
        if i in _hash_map:
            return True
        else:
            _hash_map[i] = 1
    return False