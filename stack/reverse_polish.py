# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import operator


def x(tokens):
    opt = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    s = []
    for token in tokens:
        if token in opt:
            s.append(int(opt[token](s.pop(-2), s.pop(-1))))
        else:
            s.append(int(token))
    return s[0]

"""
POLISH NOTATION Y ASUM E
AMEN QAYLOV STUGIR ARDYOQ AYN OPERATOR E TE TIV YST DRA KATARIR
1) ETE OPERATOR E VERCRA VERJIN 2 ELEMENTY(JNJELOV) U KATARIR GORCOXUTYUNY
2) ETE TIV E UXXAKI AVELACRA
"""

print(x(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
