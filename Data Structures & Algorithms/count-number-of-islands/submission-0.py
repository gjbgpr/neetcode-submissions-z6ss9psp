class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    islands += 1
                    self.dfs(row, col, ROWS, COLS, grid)

        return islands
    
    def dfs(self, row, col, ROWS, COLS, grid) -> None:
        if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == '0':
            return
        
        grid[row][col] = '0'
        self.dfs(row + 1, col, ROWS, COLS, grid)
        self.dfs(row, col + 1, ROWS, COLS, grid)
        self.dfs(row - 1, col, ROWS, COLS, grid)
        self.dfs(row, col - 1, ROWS, COLS, grid)