# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150


def reverse_array(arr, k):
    k = k % len(arr) # for effective rotation count, because if k > len(arr): example: arr = [1,2,3,4], k = 5 then k = 5 % 4 = 1
    arr[:] = arr[-k:] + arr[:-k]