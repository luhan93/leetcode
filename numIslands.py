class Solution:
    '''
    bsf
    '''
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        q_row = [i]
        q_col = [j]
        while len(q_row) != 0:
            i = q_row.pop(0)
            j = q_col.pop(0)
            grid[i][j] = 0
            if i > 0 and grid[i - 1][j] == '1':
                q_row.append(i - 1)
                q_col.append(j)
            if i < len(grid) - 1 and grid[i + 1][j] == '1':
                q_row.append(i + 1)
                q_col.append(j)
            if j > 0 and grid[i][j - 1] == '1':
                q_row.append(i)
                q_col.append(j - 1)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
                q_row.append(i)
                q_col.append(j + 1)

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        if i > 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j)
        if j > 0 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1)
        if i < len(grid)-1 and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j)
        if j < len(grid[0])-1 and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1)
        return

x = Solution()
print(x.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))