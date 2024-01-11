def checkRecord(s: str) -> bool:
    a_cnt = s.count('A')
    l_cnt = s.count('LLL')
    return a_cnt < 2 and l_cnt == 0
