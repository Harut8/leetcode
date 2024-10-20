# https://leetcode.com/problems/container-with-most-water/

### FULLY DONE ###
def max_area(heights):
    lft, rgt = 0, len(heights) - 1
    _max_area = 0
    while lft < rgt:
        hg = min(heights[lft], heights[rgt])
        ln = rgt - lft
        _max_area = max(_max_area, hg * ln)
        if heights[lft] < heights[rgt]:
            lft += 1
        else:
            rgt -= 1

    return _max_area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
"""
VERCNENQ 2 POINTER
EV HASHVENQ AREA N
AYSINQN HEIGHT * WIDTH
BAYC HEIGHT Y ANPAYMAN 2 HEIGHT RIC POQRN E
QANI VOR MIAYN NRA EV MECI ARANQY KAROX E JUR HAVAQVEL
U AMEN ANGAM HASHVEL NOR MAKERES EV VERCNEL MECAGUYNY
EV HARC INCHPES SHARUNAKEL AYSL QAYLERY
QANI VOR MENQ PETQ LEFT +1 EV RIGHT -1 ANENQ
APA WIDTH Y AMEN QAYLOV POQRANALU E
AYD ISK PATCHAROV PETQ E LEFT + 1 ANEL MIAYN ayn DEPQUM
ETE MEZ PETQ E GTNENQ DZAX KOXMIC AVELI BARCRY VORPESZI AREA N MECANA
"""