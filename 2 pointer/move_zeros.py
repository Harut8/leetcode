# https://leetcode.com/problems/move-zeroes

def move_zeros(nums):
    i = j = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1
    return nums
print(move_zeros([0,1,0,3,12]))


"""
ETE 0 CHI UXXAKI ARAJ ENQ GNUM EV SWAPP ENQ ANUM
ETE 0 E UXXAKI I += 1 ENQ ANUM
AYSINQN J IN PAHUM E VERJIN 0 I TEXY VORY PETQ E SWAP ANENQ
ete i rd andamy 0 che apa j += 1 vor hasnenq hajordin
"""