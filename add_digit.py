def addDigits(num: int) -> int:
    while num > 9:
        cur = num
        new_num = 0
        while cur > 0:
            cur, r = divmod(cur, 10)
            new_num += r
        num = new_num
    return num
