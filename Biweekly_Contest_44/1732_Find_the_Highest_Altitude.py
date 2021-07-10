class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        curr = 0
        for i in range(len(gain)):
            curr = curr + gain[i]
            mx = max(curr, mx)
        return mx	
