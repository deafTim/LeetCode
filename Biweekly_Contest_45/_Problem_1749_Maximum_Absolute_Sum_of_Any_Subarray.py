class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mn = sum(nums)
        mx = sum(nums)
        s = 0
        for i in range(len(nums)):
            mn = min(s, mn)
            mx = max(s, mx)
            s += nums[i]
        return mx-mn
