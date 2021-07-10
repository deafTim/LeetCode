class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        # we create set of all possible squares
        squares = set([i**2 for i in range(1,n+1)])
        # here we should not check whether or not i==j
        # there are no triples with equal a and b
        for i in range(1, n+1):
            for j in range(1,n+1):
                num = i**2+j**2
                if num in squares:
                    ans += 1
        return ans
