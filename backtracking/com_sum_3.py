# https://leetcode.com/problems/combination-sum-iii/submissions/

def combinationSum3(k, n):
    res = []
    def backtrack(summ, current_sub, start):
        if len(current_sub) == k and summ == n:
            res.append(current_sub.copy())
            return
        if summ > n or len(current_sub) == k:
            return
        for i in range(start, 10):
            current_sub.append(i)
            backtrack(summ + i, current_sub, i + 1)
            current_sub.pop()
    backtrack(0, [], 1)
    return res
"""
KRKIN OGTVUM ENQ BACKTRACK IC EV COMBINATIONNERI GAXAPRIC
AMEN QAYLI JAMANAK ADD ANENQ CURENT EL IN EV HASHVENQ SUMM
ETE SUMM = K EV COM EL RI QANAKY = K UREMN HASANQ
"""