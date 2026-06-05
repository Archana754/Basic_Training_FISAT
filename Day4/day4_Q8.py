#https://leetcode.com/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n=len(nums)
        s=sum(nums[:k])
        m=s
        for i in range(1,n-k+1):
            s=s-nums[i-1]+nums[i+k-1]
            m=max(m,s)
        return(m/k)