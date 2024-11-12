# https://leetcode.com/problems/generate-parentheses/

def generate_parentheses(n):
    def add_backtrace(s, open_count, close_count):
        print(s)
        if open_count == 0 and close_count == 0:
            res.append(s)
        else:
            if open_count > 0:
                add_backtrace(s + '(', open_count - 1, close_count + 1)
            if close_count > 0:
                add_backtrace(s + ')', open_count, close_count - 1)

    res = []
    add_backtrace('', n, 0)
    return res


print(generate_parentheses(3))
