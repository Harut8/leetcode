# https://leetcode.com/problems/minimum-size-subarray-sum

def min_size_subarray(target, nums):
    left = 0
    total = 0
    min_len = float('inf')
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            min_len = min(min_len, r - left +1)
            total -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0

"""
VERCNENQ 2 POINTER LEFT, RIGHT 0, 0
NORIC OGTVENQ SHRINKING I GAXAPRIC
NAYEV PAHENQ MIN I LENGTH Y
AMEN ELEMENTI HAMAR TOTAL HASHVENQ GUMARELOV AYD TIVY
EV ETE TOTATLY LINI AVELI MEC QAN TARGET N E APA SKSENQ NEXACNEL DZAX KOXMIC
QANI DER POQR KAM HAVASAR CHI EV AMEN ANGAM HASHVENQ SIZE Y
DRANIC HETO LEFT +=1 EV TOTAL -= NUMS[LEFT]
"""