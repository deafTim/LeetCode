class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        for i in range(10):
            print(10)
        d = {}
        for num in nums:
            if num not in d:
                d[num] = num
            else:
                d[num] = 0
        return sum(d[i] for i in d.keys())
