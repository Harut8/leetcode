# https://leetcode.com/problems/permutations/

def permutations(nums):
    res = []
    def backtracking(current_permutation):
        if len(current_permutation) == len(nums):
            res.append(current_permutation.copy())
            return
        for i in range(len(nums)):
            if nums[i] in current_permutation:
                continue
            current_permutation.append(nums[i])
            backtracking(current_permutation)
            current_permutation.pop()
    backtracking([])
    return res
print(permutations([1, 2, 3]))
"""
I TARBERUTYUN SUBSET I
MENQ SARQUM ENQ PERMUTATION EV DA NSHANAKUM E
VOR CHVERCNELU DEPQ CHKA
ETE UNENQ TANDZ XNDZOR MANDARIN
APA AMEN QAYLIN PETQ E VERCNENQ ELEMENT EV LCNENQ ARKXI MEJ
BAYC QANI VOR KA AYNPISI DEPQER VOR ELEMENTY ARDEN ISK KA ARRAY I MEJ
PETQ E AYN BAC TOXNENQ
ORINAK [1, 1, 2] DEPQ CHSTANALU HAMAR 
PERMUTATION I DEPQUM MENQ MISHT PETQ E YNTRENQ VOREVE ELEMENT
https://manvityagi770.medium.com/backtracking-part-3-permutations-problems-2b2740da840f
"""

