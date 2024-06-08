""" 
Given an m x n 2d binary grid grid which represents a map of '1' s(land) and '0's (water). return the number of the islands.

An island is surrounded by water and is formed by coneecting adjecent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water

Example:
input: grid = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]

output: 1
"""

def numIsland(grid: list[list[str]]) -> int:
    #n = panjang dari grid
    #m = panjang dari grid[0]
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= m or j  < 0 or j >= n or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)
        

    num_islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                num_islands += 1
                dfs(i, j)
    
    return num_islands

grid = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]

print(numIsland(grid))