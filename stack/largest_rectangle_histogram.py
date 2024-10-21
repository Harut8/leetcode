# https://leetcode.com/problems/largest-rectangle-in-histogram/

def largest_rectangle_area(heights):
    stack = [] # increasing order
    max_area = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h_idx = stack.pop()
            height = heights[h_idx]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * w)
        stack.append(i)
    while stack:
        h_idx = stack.pop()
        height = heights[h_idx]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * w)
    return max_area
"""
NAIVE TARBERAKOV KAROX ENQ AMEN BAR I HAMAR
UXXAKI NAYEL AJ EV DZAX U GTNEL MECAGUYN HNARAVOR TARBERAKY
BAYC SA KLINI O(N^2)
AYD ISK PATCHAROV MENQ KAROX ENQ
OGTVEL AYN GAXARPARIC VOR HISTOGRAM I AREA N
MECANUM E BAR I ERKARUTYUNY MEC E
AYSINQN PAHENQ STACK VOR KLINI ACHMAN KARGOV
EV ETE MER I RD ELEMENTY LINI AVELI POQR QAN STACK I VERJIN LEMENTN E
APA MAQRUM ENQ STACK Y HASHVELOV AREA NER EV MAXIMAL I BERUM
INCREASING ORDER Y MEZ TUYL E TALIS VSTAH LINEL VOR I - STACK[-1] -1 RD ELEMENTY NUYNPES BAVARARUM E
"""