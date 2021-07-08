class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def summ(n):
            s = 0
            while n>0:
                s += (n%10)
                n //= 10
            return s
        counter = [0 for i in range(46)]
        for i in range(lowLimit, highLimit+1):
            counter[summ(i)] += 1
        return max(counter)
