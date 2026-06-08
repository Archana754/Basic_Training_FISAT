#https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n == 0:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return n
        else:
            s, e = 0, n - 1
            m = 0
            while (s <= e):
                m = (s + e) // 2
                if (nums[m - 1] < nums[m] > nums[m + 1]):
                    return m
                elif (nums[m] < nums[m + 1]):
                    s = m + 1
                else:
                    e = m - 1

