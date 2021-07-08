class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> int:
        while len(adjacentPairs)>1:
            l=0
            h = defaultdict(tuple)
            while l < len(adjacentPairs):
                num0 , num1 = adjacentPairs[l][0], adjacentPairs[l][-1]
                if num0 not in h and num1 not in h:
                    h[num0], h[num1] = (l, 0), (l,-1)
                    l += 1
                elif num0 in h:
                    indx, side = h[num0][0], h[num0][1]
                    if side == 0:
                        adjacentPairs[indx] = adjacentPairs[l][::-1]+adjacentPairs[indx][1:]
                        h[num1] = (indx, side)
                    if side == -1:
                        adjacentPairs[indx] = adjacentPairs[indx][:-1] + adjacentPairs[l]
                        h[num1] = (indx, side)
                    adjacentPairs.pop(l)
                elif num1 in h:
                    indx, side = h[num1][0], h[num1][1]
                    if side == 0:
                        adjacentPairs[indx] = adjacentPairs[l]+adjacentPairs[indx][1:]
                        h[num0] = (indx, side)
                    if side == -1:
                        adjacentPairs[indx] = adjacentPairs[indx][:-1] + adjacentPairs[l][::-1]
                        h[num0] = (indx, side)
                    adjacentPairs.pop(l)
        return adjacentPairs[0]
