# https://leetcode.com/problems/can-place-flowers?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0] # add 0 at both ends to handle edge cases
        for i in range(1, len(flowerbed)-1):
            if sum(flowerbed[i-1:i+2]) == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return n <= 0