# https://leetcode.com/problems/daily-temperatures/


def daily_temperature(temperatures):
    _res = [0] * len(temperatures)
    _stack = []
    for i, t in enumerate(temperatures):
        while _stack and t > temperatures[_stack[-1]]:
            _res[_stack[-1]] = i - _stack[-1]
            _stack.pop()
        _stack.append(i)
    return _res
