#eetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def backspace(s):
            st = []
            for ch in s:
                if ch != '#':
                    st.append(ch)
                else:
                    if st:
                        st.pop()
            return st

        rs = backspace(s)
        rt = backspace(t)
        if rs == rt:
            return True
        return False

