# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150


def reverse_array(arr, k):
    k = k % len(arr)
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    reverse(0, len(arr) - 1)
    reverse(0, k - 1)
    reverse(k, len(arr) - 1)
    return arr