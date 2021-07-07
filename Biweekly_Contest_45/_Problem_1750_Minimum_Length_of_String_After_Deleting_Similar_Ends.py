class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                break
            while l<len(s)-1 and s[l]==s[l+1]: l += 1
            while r>0 and l<=r and s[r]==s[r-1]: r -= 1
            if l<r:
                l += 1
                r -= 1
        return r-l+1
