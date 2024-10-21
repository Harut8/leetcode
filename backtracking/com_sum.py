# https://leetcode.com/problems/combination-sum/
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(current_sub, start, rem):
            if rem == 0:
                res.append(current_sub[:])
                return
            for i in range(start, len(candidates)):
                if rem - candidates[i] >= 0:
                    current_sub.append(candidates[i])
                    backtrack(current_sub, i, rem - candidates[i])
                    current_sub.pop()

        backtrack([], 0, target)
        return res

"""
QANI VOR COM Y IRENIC ENTADRUM E NUYN ELEMENTI KRKNUTYUN MI QANI ANGAM
ORINAK [2,2,3] APA MEZ PETQ CHE I + 1 ANEL AMEN QAYLIC VOROVHETEV AYD
DEPQUM KSTANANQ SUBSET I GAXAPRY
MYUS KOXMIC MEZ PETQ EN MIAYN ELEMENTNERY VORONQ POTENCIAL KAROX ENQ KANDIDANT LINEL
AYSINQN NRANQ VORONQ KARAN POQRACNEN REM I CHAPY
"""