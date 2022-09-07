class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = 0
        counts = [[0]*n for _ in range(m)]
        for i in range(n):
            counts[0][i] = 1
        for j in range(m):
            counts[j][0] = 1 
        for i in range(1,m):
            for j in range(1,n):
                counts[i][j] += (counts[i-1][j] + counts[i][j-1])
        return counts[m-1][n-1]
                
        
# 모든 matrix 필요 x 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = 0
        counts = [1]*n
        for i in range(1,m):
            left = 1 
            for j in range(1,n):
                counts[j] = (counts[j] + left)
                left = counts[j]
        return counts[n-1]
                
