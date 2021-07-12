class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                val = nums[i]*nums[j]
                d[val]+=1
        ans = 0
        for v in d.values():
            if v>1:
                ans+=v*(v-1)/2
        return int(ans*8)
