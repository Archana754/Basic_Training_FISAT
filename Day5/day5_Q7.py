#https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        s,e=0,len(nums)-1
        m=0
        while(s<=e):
            m=(s+e)//2
            if(nums[m]==target):
                return m
            elif(target>nums[m]):
                s=m+1
            else:
                e=m-1
        else:
            return s