def missing_number(nums):
    n = len(nums)
    # sum of numbers from 0 to n  is n(n+1)/2
    return n * (n + 1) // 2 - sum(nums)
