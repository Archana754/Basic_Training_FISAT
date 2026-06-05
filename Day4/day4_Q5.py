#https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i<j:
            if(s[i]!=s[j]):
                skip_left=s[i+1:j+1]
                skip_right=s[i:j]
                if skip_left==skip_left[::-1] or skip_right==skip_right[::-1]:
                    return True
                else:
                    return False
            i+=1
            j-=1
        return True