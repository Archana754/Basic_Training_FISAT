#https://leetcode.com/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        st=[]
        for curr in nums2:
            while st and st[-1]<curr:
                ele=st.pop()
                d[ele]=curr
            st.append(curr)
        while st:
            d[st.pop()]=-1
        res=[]
        for i in nums1:
            res.append(d[i])
        return res