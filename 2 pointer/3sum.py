### FULLY DONE ###
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lft = i + 1
            rgt = len(nums) - 1
            while lft < rgt:
                summ = nums[lft] + nums[rgt] + nums[i]
                if summ < 0:
                    lft +=1
                elif summ > 0:
                    rgt -=1
                else:
                    res.append([nums[i], nums[lft], nums[rgt]])
                    while lft<rgt and nums[lft] == nums[lft + 1]:
                        lft+=1
                    while lft<rgt and nums[rgt] == nums[rgt - 1]:
                        rgt-=1
                    lft +=1
                    rgt -=1
        return res

"""
XNDIRY BAVAKANIN NMAN E 2 SUMM IN BAYC SORTAVORVACI DEPQUM
AYSINQN KAROX ENQ OGTVEL 2 SUMM I LUCUMIC BAYC SORT IC HETO
MITQY HETEVYALN E 
MEZ PETQ EN 3 TVER VORONC GUMARY 0 E
AYSINQN GONE 3 TIV PETQ EN***
NUMS I BOLOR TVERI HAMAR KAROX ENQ PORCEL LUCEL 2 SUMM I XNDIRY
AYSINQN VERCNENQ I RD ELEMEMENTY EV LUCENQ 2 SUMM I XNDIRY
BAYC KAREVOR KET PETQ E VOR BOLOR SUBSET RY LINEN TARBER
AYSINQN [-1, -1, 0, 1, 2] I DEPQUM ERB UNENQ 2 HAT -1
KSTANANQ 2 LUCUMNER TARBER IDX NEROV BAYC NUYN -1 OV VORY TUYLATRELI CHE
DRA HAMAR: if i > 0 and nums[i] == nums[i - 1]: continue
EV 2 RD PAYMANY
[-2, 0, 0, 2, 2] I DEPQUM
nums[0] = -2
nums[1] = 0
nums[4] = 2
Triplet: (-2, 0, 2)
nums[0] = -2
nums[2] = 0
nums[3] = 2
Triplet: (-2, 0, 2)
AYSINQN UNENQ 2 TARBER IDX NER BAYC NUYN TVERY VORY KRKIN ANTUYLATRELI E
DRA HAMAR
while lft<rgt and nums[lft] == nums[lft + 1]:
    lft+=1
while lft<rgt and nums[rgt] == nums[rgt - 1]:
    rgt-=1
"""