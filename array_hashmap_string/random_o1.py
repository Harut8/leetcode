# https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1713263042/?envType=study-plan-v2&envId=top-interview-150
import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.nums.append(val)
        self.dic[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        idx = self.dic[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.dic[last] = idx
        self.nums.pop()
        self.dic.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)