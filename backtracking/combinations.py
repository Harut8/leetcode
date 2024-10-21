# https://leetcode.com/problems/combinations/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(start, curr_sub):
            if len(curr_sub) == k:
                res.append(curr_sub[:])
                return
            for i in range(start, n + 1):
                curr_sub.append(i)
                backtrack(i+1, curr_sub)
                curr_sub.pop()
        backtrack(1, [])
        return res

"""
COMBINATION I MEJ AMEN ELEMEMT I DIRQ KAREVOR CHE
AYSINQN VONC GRVAC E BASE I MEJ HERTAKANUTYUNY KAREVOR CHE
MENQ CHENQ UZUM BOLOR ELEMENTNERY BOLOR TEXERY DNENQ
AYL PETQ E VERCNENQ ORINAK ELAK HETO YNTRENQ KAM BANAN KAM XNDZOR
MEZ HET 2 RD ANGAM ELAK PETQ CHE
COMBINATION I DEPQUM MENQ KAROX ENQ CHNTREL ELEMENT
https://manvityagi770.medium.com/backtracking-part-4-combinations-problems-i-5831f4ffb9ed
"""