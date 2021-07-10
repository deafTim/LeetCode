class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        for i in range(1,len(encoded)):
            encoded[i] ^= encoded[i-1]
        xor = 0
        for i in range(1+len(encoded)):
            xor ^= (i+1)
        for i in range(len(encoded)):
            xor ^= encoded[i]
        ans = [xor]
        for i in range(len(encoded)):
            ans.append(xor^encoded[i])
        return ans
