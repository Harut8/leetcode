#mhttps://leetcode.com/problems/subsets/

def subsets(nums):
    res = []
    def backtrack(current_subset, idx):
        res.append(current_subset.copy())
        for i in range(idx, len(nums)):
            current_subset.append(nums[i])
            backtrack(current_subset, i + 1)
            current_subset.pop()
    backtrack([], 0)
    return res

print(subsets([1, 2, 3]))

"""
PATKERACNENQ UNENQ DATARK ARKX VORI MEJ PETQ E DNENQ
TAMDZ, XNDZOR, MANDARIN
AMEN QAYLI KAROX ENQ VERCNEL ELEMENT KAM CHVERCNEL
EV SUBSET I MEJI LEMENTNERI HERTAKANUTYUNY KAP CHUNI
[TANDZ, XNDZOR] TE [XNDZOR, TANDZ] NUYNN E
AYSINQN VERCNUM ENQ DATARK ARKX
EV AVELACNUM ENQ VOREVE MIRG EV HAJORD QAYLIN BACI DRANIC
KAROX ENQ YNTREL MNACACIC AYSINQN MEZ PETQ E IDX VOR TRACK ANENQ AYN
INCHPES NAYEV VORPESZI HAJORD MRGOV KAROXANANQ ANEL NUYN BANY MEZ PETQ E
"""