# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150

def simplify(path):
    stack = []
    for ch in path.split('/'):
        if ch == "" or ch == ".":
            continue
        elif ch == '..':
            if stack:
                stack.pop()
        else:
            stack.append(ch)

    return '/' + '/'.join(stack)
print(simplify("/home//foo/./bar/../baz/"))
"""
. Y NSHANAKUM E MNAL NUYN DIR UM
.. Y NSHANAKUM E BARCRANAL PARENT I PATH
ISK / EV /// NUYNN EN NSHANAKUM
AYSINQN ETE MENQ UNENQ /HARUT//./FOO/BAR/../BAZ
SA NUYNN E INCH VOR HARUT/FOO/BAR I C HETO HET GNAL HARUT/FOO EV MTNEL /BAZ
"""