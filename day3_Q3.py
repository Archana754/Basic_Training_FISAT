# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1=0
        for i in nums:
            x1=x1^i
        return x1
