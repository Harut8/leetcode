# https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150


def isHappy(n: int) -> bool:
    def f(x):
        s = 0
        while x:
            _rem = x % 10
            s += _rem ** 2
            x = x // 10
        return s

    while n != 1 and n != 4:
        n = f(n)
    return n == 1

print(isHappy(11))