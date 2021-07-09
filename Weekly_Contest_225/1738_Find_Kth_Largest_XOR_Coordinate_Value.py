class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(1,m):
                matrix[i][j] = matrix[i][j] ^ matrix[i][j-1]
        for i in range(1, n):
            for j in range(m):
                matrix[i][j] = matrix[i][j] ^ matrix[i-1][j]
        arr = [num for row in matrix for num in row]
        return sorted(arr)[-k]
                    
