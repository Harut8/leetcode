# https://leetcode.com/problems/contains-duplicate/

def contains_duplicate(nums):
    """
    Time Complexity: O(n) - converting to set requires iterating over nums once
    Space Complexity: O(n) - storing unique elements in set
    """
    return len(nums) != len(set(nums))


def contains_duplicate_2(nums):
    """
    Time Complexity: O(n) - iterate through array once 
    Space Complexity: O(n) - storing elements in hash map
    """
    _hash_map = dict()
    for i in nums:
        if i in _hash_map:
            return True
        else:
            _hash_map[i] = 1
    return False

def contains_duplicate_3(nums):
    """
    Time Complexity: O(nlogn) - sorting dominates runtime
    Space Complexity: O(1) - sorting in place with constant extra space
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False


nums = [1,2,3,1]
print(contains_duplicate_3(nums))