class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        old = 0
        newGrid = [[0] * len(grid[0])] * len(grid[0])
        colGrid =  [[grid[j][i] for j in range (len (grid))] for i in range (len (grid[0]))]
        colMax = [0] * len(colGrid)
        rowMax = [0] * len(grid)
        for i in range(len(colGrid)):
            colMax[i] = max(colGrid[i])
        for i in range(len(grid)):    
            rowMax[i] = max(grid[i])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                newGrid[i][j] = min(rowMax[i], colMax[j])
                total += newGrid[i][j]
                old += grid[i][j]       
        return total - old