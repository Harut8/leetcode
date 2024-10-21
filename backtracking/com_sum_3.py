# https://leetcode.com/problems/combination-sum-iii/submissions/

res = []
k = 3
n = 7
def backtrack(curr, start, rem):
    if len(curr) == k and rem == 0:
        res.append(curr[:])
    if len(curr) > k or rem < 0:
        return
    for i in range(start, 10):
        curr.append(i)
        backtrack(curr, i + 1, rem - i)
        curr.pop()
    backtrack([],1, n)
    return res
"""
KRKIN OGTVUM ENQ BACKTRACK IC EV COMBINATIONNERI GAXAPRIC
AMEN QAYLI JAMANAK ADD ANENQ CURENT EL IN EV HASHVENQ SUMM
ETE SUMM = K EV COM EL RI QANAKY = K UREMN HASANQ
"""