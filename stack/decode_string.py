# https://leetcode.com/problems/decode-string/

def decode_string(s):
    stack = [] # store previous string and repeating number
    res_str = ""
    repeating_num = 0
    for ch in s:
        if ch.isdigit():
            repeating_num = repeating_num * 10 + int(ch)
        elif ch == '[':
            stack.append((res_str, repeating_num))
            res_str = ""
            repeating_num = 0
        elif ch == ']':
            prev_str, repeat_num = stack.pop()
            res_str *= repeat_num
            res_str = prev_str + res_str
        else:
            res_str += ch
    return res_str

print(decode_string("3[a]2[bc]"))
"""
AYS XNDIRY NMAN E CALCULATOR I XNDRIN
AMEN QAYLI HNARAVOR E 4 DEPQ
ETE TIV E ETE [ ETE ] ETE CHAR
TVI DEPQUM PETQ E VERCNEL SARQEL TIV EV PAHEL
ETE [ APA PAHEL NAXORD RESULTY STACK I MEJ AVELI KONKRET
RESULT_STR EV REPEAT_TIME
ETE ] APA JNJEL DRANQ YST HERTAKANUTYAN
GUMAREL LAST_STR VORY VOR JNJEL ENQ NOR EV AVELACNENQ DRANQ RESULT_STR*REPEAT_TIME
"""