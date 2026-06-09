#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '{':
                st.append('}')
            elif ch == '(':
                st.append(')')
            elif ch == '[':
                st.append(']')
            elif len(st) == 0 or st.pop() != ch:
                return False
        return len(st) == 0





