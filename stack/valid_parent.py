# https://leetcode.com/problems/valid-parentheses/

def is_valid(parents):
    s = []
    open_closed = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for ch in parents:
        if ch in open_closed:
            s.append(ch)
        else:
            _last_ch = s.pop() if s else None
            if not _last_ch or open_closed[_last_ch] != ch:
                return False
    return True if not s else False
print(is_valid("(][]{}"))
"""
OGTAGORCUM ENQ STACK VOR PAHENQ VERJIN BACOX SCOPE Y
AMEN QAYLI JMNK ETE AYN BACOX E AVELACNUM ENQ ETE PAKOX E 
PORCUM ENQ JNJEL STACK IC ETE CHKA NONE ENQ TALIS
EV ETE AYD ELEMENTY I TAK GTNVOX PAKOX SCOPE Y CHISHT CHE AYSINQN
CHI HAMNKNUM MER CH I HET APA SXAL EQANI VOR MENQ GITENQ VOR 
STACK I VERJIN ELEMENTY BACOX E EV YST OPEN_CLOSED I
MENQ KAROX ENQ VOROSHEL TE VORY PETQ E IRAKANUM PAKER
"""