#https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        s , e =1 ,x
        while( s<=e):
            m=(s+e)//2
            if x==m*m:
                return m
            elif x>m*m :
                s=m+1
            else:
                e=m-1
        return e

