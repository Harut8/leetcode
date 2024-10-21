# https://leetcode.com/problems/longest-consecutive-sequence/


nums = [100, 4, 200, 1, 3, 2]

def solution(_nums):
    _nums = set(nums)
    _longest = 0 # longest sequence length found so far
    for _n in _nums:
        # ensure, that n CAN BE start of a sequence
        if _n - 1 not in _nums:
            # that means, that current length is 1
            _length = 1
            # search for next numbers in sequence
            while _n + 1 in _nums:
                _n += 1
                _length += 1
            _longest = max(_length, _longest)

    return _longest

"""
NAX SARQENQ SET VORPESZI DUPLICATE IC PRCNENQ
EV PARZ E VOR ELEMENTY KAROX E LINEL POTENCIAL ARRAY I SKIZB ETE 
N - 1 RD ELEMENTY CHKA SET I MEJ
EV QANI DER DRA HAJORD ELEMENTY KA ARRAY I MEJ APA DA
HAMARVUM E HAJORDAKAN 
EV AMEN QAYLIN UXXAKI MECACNUM ENQ
"""




