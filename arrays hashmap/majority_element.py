# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
from collections import defaultdict
nums = [3,2,3]
count_map = defaultdict(int)
majority_count = len(nums) // 2

def majority_element(nums):
    for num in nums:
        count_map[num] += 1
        if count_map[num] > majority_count:
            return num
print(majority_element(nums))
"""
MER ARRAY I MEJ AMEN ELEMENT KAROX E LINEL MAJOR
MAJOR E ETE DRA QANAKY SHAT E QAN N/2 Y VORTEX N Y ARRAY CHAPN E
AMEN QAYLIN KAROX ENQ HAMAREL VOR MAJOR Y NOR ELEMENT E
GTNELU DEPQUM + ANEL 1
"""