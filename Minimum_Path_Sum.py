class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # row
        n = len(grid[0]) # cols
        temp = [[0 for j in range(n)] for i in range(m)]
        temp[0][0] = grid[0][0]
        for i in range(1,n):
            temp[0][i] = temp[0][i-1] + grid[0][i]
        for i in range(1,m):
            temp[i][0] = temp[i-1][0] + grid[i][0]
            
        for i in range(1,m):
            for j in range(1,n):
                temp[i][j] = grid[i][j]+ min(temp[i-1][j],temp[i][j-1])
        
        return temp[m-1][n-1]
