# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    _map = {}
    for i, el in enumerate(nums):
        if el in _map and abs(_map[el] - i) <= k:
            return True
        _map[el] = i # Always update for new elements otherwise it will cause bug
    return False

print(containsNearbyDuplicate([1,2,3,1], 3))