# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

def remove_dup_from_sorted_2(nums):
    """
    This function takes a sorted array and removes duplicates,
    allowing up to two duplicates. It returns the length of the
    resulting array.

    The solution uses the two-pointer approach. The slow pointer
    points to the last element that has been written to the new
    array (i.e., the new array is from index 0 to slow - 1), and
    the fast pointer points to the current element being processed.

    If the current element is different from the last element and
    the element before the last element, then the current element
    should be written to the new array. Otherwise, the current element
    should be skipped.

    The time complexity is O(n), where n is the length of the input
    array. The space complexity is O(1), since no additional space
    is used.
    """
    n = len(nums)
    if n <= 2:
        return n
    write = 2
    for read in range(2, n):
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    return write