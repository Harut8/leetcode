# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_smallest = float('inf')
        second_smallest = float('inf')
        for n in nums:
            if n <= first_smallest:
                first_smallest = n  # find first
            elif n <= second_smallest:
                second_smallest = n  # second because alreadyfirst condition false
            else:
                return True  # n > second > first → triplet found
        return False

