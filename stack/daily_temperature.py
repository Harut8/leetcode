# https://leetcode.com/problems/daily-temperatures/


def daily_temperature(temperatures):
    stack = []
    res = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            el = stack.pop()
            res[el] = i - el
        stack.append(i)

    return res

print(daily_temperature([73, 74, 75, 71, 69, 72, 76, 73]))


"""
PAHENQ STACK VORTEX KLINEN MIAYN ELEMENTNERI IDX NERY
BAYC VORPESZI KAROXANANQ VOROSHEL TE QANI OR E PETQ SPASEL
MEZ PETQ E INCH VOR DZEVOV OGTVEL AYD STACK I ELEMENTNERIC
ORINAK ETE UNENQ 73,72,75 
SA NSHANAKUM E VOR PETQ E STANANQ [2, 1, 0] ARRAY VORPES PATASXAN
AYSINQN MENQ AYSTEX TESNUM ENQ VOR KA JNJELU PROCESS VORY
KAROX E LINEL MEK KAM MI QANI ANGAM AYN E WHILE I NMAN

AYSINQN PAHUM ENQ STACK VOR I MEJ KLINEN TEMPERATURE NERY YST NVAZMAN KARGI
EV ETE HANDIPI AVELI MECY HERTOV KJNJENQ EXACNERY EV KTEXADRENQ RES I MEJ
"""
