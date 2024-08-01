def nums_3_sum(nums):
    if len(nums) < 3:
        return []
    elif len(nums) == 3 and sum(nums) == 0:
        return [nums]

    nums = sorted(nums)
    solutions = []
    i = 0
    while i < len(nums) - 2:  # minus 2 for searching 3 numbers
        if i > 0 and nums[i] == nums[i - 1]:  # Skip any duplicates
            i += 1
            continue

        j = i + 1
        k = len(nums) - 1
        target = 0 - nums[i]  # solving the 2 sum problem
        while j < k:
            if j > i + 1 and nums[j] == nums[j - 1]:  # Skip any duplicates
                j += 1
                continue
            if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                k -= 1
                continue
            jkSum = nums[j] + nums[k]
            if jkSum == target:  # Found pair
                solutions.append([nums[i], nums[j], nums[k]])

            if jkSum > target:
                k -= 1
            else:
                j += 1  # Advances from solution too

        i += 1

    return solutions


print(nums_3_sum([-1, 0, 1, 2, -1, -4]))
