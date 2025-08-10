# https://leetcode.com/problems/merge-sorted-array?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers
        m -= 1
        n -= 1
        # Initialize a pointer for the result
        i = m + n + 1

        # Merge two sorted arrays
        while m >= 0 and n >= 0:
            # If the current element in nums1 is greater than the current element in nums2
            if nums1[m] > nums2[n]:
                # Place the element from nums1 at the end of the result
                nums1[i] = nums1[m]
                # Move the pointer in nums1 to the left
                m -= 1
            else:
                # Place the element from nums2 at the end of the result
                nums1[i] = nums2[n]
                # Move the pointer in nums2 to the left
                n -= 1
            # Move the pointer in the result to the left
            i -= 1

        # If there are remaining elements in nums2, copy them to the result
        while n >= 0:
            nums1[i] = nums2[n]
            # Move the pointer in nums2 to the left
            n -= 1
            # Move the pointer in the result to the left
            i -= 1

        return nums1


print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))