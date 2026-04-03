class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    queue.append([row, col])
        
        result = 0
        while queue:
            row, col = queue.popleft()
            result += (self.add(row + 1, col, grid, ROWS, COLS) +
                        self.add(row - 1, col, grid, ROWS, COLS) +
                        self.add(row, col + 1, grid, ROWS, COLS) +
                        self.add(row, col - 1, grid, ROWS, COLS))
        return result
    
    def add(self, row, col, grid, ROWS, COLS):
        if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] == 0:
            return 1
        return 0