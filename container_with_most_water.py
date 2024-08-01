# https://leetcode.com/problems/container-with-most-water/

def max_area(heights):
    lft, rgt = 0, len(heights) - 1
    _max_area = 0
    while lft < rgt:
        _max_area = max(_max_area, heights[lft] * (rgt - lft))

        if heights[lft] < heights[rgt]:
            lft += 1
        else:
            rgt -= 1

    return _max_area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
