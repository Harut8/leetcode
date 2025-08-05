class Solution:
  def longestSubarray(self, nums: list[int]) -> int:
    """
    This solution works by maintaining a sliding window of elements in the array.
    The window is defined by two pointers, l and r, which represent the start and end of the window respectively.

    The goal is to find the longest subarray with at most one zero. To do this, we keep track of the number of zeros in the window using the variable zeros.

    We start by iterating through the array and for each element, we check if it's a zero. If it is, we increment the zeros variable. If the number of zeros is greater than one, we know that the window is no longer valid, so we slide the window to the right by incrementing l. If the element at the new l index is a zero, we decrement the zeros variable to keep track of the correct number of zeros in the window.

    At the end of the iteration, we return the length of the longest subarray with at most one zero, which is given by len(nums) - l - 1.

    The time complexity of this solution is O(n), where n is the length of the input array, and the space complexity is O(1), since we only use a constant amount of space to store the variables.
    """
    l = 0
    zeros = 0

    for num in nums:
      if num == 0:
        zeros += 1
      if zeros > 1:
        if nums[l] == 0:
          zeros -= 1
        l += 1

    return len(nums) - l - 1