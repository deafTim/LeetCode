class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        mxlen = 0
        for rec in rectangles:
            mxlen = max(mxlen, min(rec[0],rec[1]))
        counter = 0
        for rec in rectangles:
            if min(rec[0],rec[1])==mxlen:
                counter += 1
        return counter
