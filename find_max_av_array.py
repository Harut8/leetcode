def findMaxAverage(nums: list[int], k: int) -> float:
    cur_summ = cnt = 0
    ans = -float("inf")
    for i in range(len(nums)):
        cnt += 1
        cur_summ += nums[i]

        if cnt == k:
            ans = max(ans, cur_summ / k)
        if cnt > k:
            cur_summ -= nums[i - k]
            ans = max(ans, cur_summ / k)
    return ans
