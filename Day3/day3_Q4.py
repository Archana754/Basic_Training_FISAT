# https://leetcode.com/problems/power-of-two/
# time complexity : logn

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        while n:
            if n==1:
                return True
            elif n%2!=0:
                return False
            else:
                n=n//2
                
# if n<1:
#     return False
# if n&(n-1)==0:
#     return True
# else:
#     return Flase

