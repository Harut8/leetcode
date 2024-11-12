# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    last = 0 # last index of unique elements
    for i in range(1, len(nums)):
        if nums[i] != nums[last]:
            last += 1
            nums[last] = nums[i]
    print(nums)
    return last + 1

nums = [0,0,1,1,1,2,2,3,3,4]

remove_duplicates(nums)
"""
QANI VOR ARRAY Y SORT ARAC E
DA NSHANAKUM E VOR ETE MI LEMENTIC KA 2 HAT APA DRANQ IRAR HAJORDUM EN
AYSINQN PAHELOV J POINTER Y VORY CUYC KTA VERJIN UNIQUE ELEMENTY
MENQ AMEN QAYLOV STUGUM ENQ ARDYOQ NORY GTEL ENQ TE CHE
ETE GTEL ENQ POINTERY + 1 ENQ ANUM VOR POINT ANI NORIN 
EV UPDATE ENQ ANUM VERJIN UNIQUE ELEMENTIC HETO GTNVOXY ( AYSINQN SORTED I DEPQUM HENC INQY)
U KDARNAP OINT AREIN HENC I IN 
"""