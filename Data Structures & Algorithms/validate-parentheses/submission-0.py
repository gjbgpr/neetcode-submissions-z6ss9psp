class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(', ']':'[', '}':'{'}
        st = []
        for i in range(len(s)):
            if s[i] not in valid:
                st.append(s[i])
            elif not st or st.pop() != valid[s[i]]:
                return False
        
        return False if st else True