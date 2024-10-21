# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150

def calculate(expression):
    i = 0
    res = 0
    sign = 1
    stack = []
    while i < len(expression):
        ch = expression[i]
        if ch.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = 10 * num + int(expression[i])
                i += 1
            i -= 1
            res += num * sign
        elif ch == '+':
            sign = 1
        elif ch == '-':
            sign = -1
        elif ch == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif ch == ')':
            res *= stack.pop()
            res += stack.pop()
        i +=1
    return res
print(calculate("1 + 1"))
"""
MEZ PETQ KGA STACK VORTEX PAHELU ENQ MINCHEV ( NSHANY
HASHVAC RESULT Y EV NSHANY
ETE HANDIPEC ) APA DA NSHANAKUM E VOR
UNECAC RESULT Y VORY HASHVEL ENQ PAKAGCI HAMAR PETQ E BAZMAPATKEL NSHANOV
AYSINQN 1 - (2+3) I HAMAR 5 * -1 EV ARJEQY GUMARENQ UNECAC RESULT IN
VORY NUYNPES STACKUM ER QANI VOR ( KAR
NSHAN I HAMAMR SIGN VORY =1 KAM =-1 EV RESULT
"""