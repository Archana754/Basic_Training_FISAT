#https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l,r=0,0
        p=1
        cnt=0
        if k<=1:
            return 0
        while r<len(nums):
            p*=nums[r]
            while p>=k:
                p//=nums[l]
                l+=1
            cnt+=r-l+1
            r+=1
        return cnt
