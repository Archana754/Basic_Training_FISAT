#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        s,e=0,len(nums)-1
        m=0
        res=[-1,-1]
        while(s<=e):
            m=(s+e)//2
            if(nums[m]==target):
                res[0]=m
                e=m-1
            elif(target>nums[m]):
                s=m+1
            else:
                e=m-1

        s,e=0,len(nums)-1
        while(s<=e):
            m=(s+e)//2
            if(nums[m]==target):
                res[1]=m
                s=m+1
            elif(target>nums[m]):
                s=m+1
            else:
                e=m-1
        return res