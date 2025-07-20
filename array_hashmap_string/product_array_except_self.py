# https://leetcode.com/problems/product-of-array-except-self/

nums = [1, 2, 3, 4]


def product_except_self(_nums):
    n = len(_nums)
    _output = [1] * n
    _prefix_product = _suffix_product = 1
    # traverse from left to right and store previous elements product in _prefix_product
    for i in range(n):
        _output[i] = _prefix_product
        _prefix_product *= _nums[i]
    for i in range(n - 1, -1, -1):
        _output[i] *= _suffix_product
        _suffix_product *= _nums[i]
    return _output
