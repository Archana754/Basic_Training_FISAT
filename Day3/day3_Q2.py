#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum1=n*(n+1)//2
        sum2=0
        for i in nums:
            sum2+=i
        return sum1-sum2

# l=len(nums)
# x1,x2=0,0
# for i in range(l+1):
#     x1=x1^i
# for i in nums:
#     x2=x2^i
# return x1^x2
