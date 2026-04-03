class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return self.bfs(row, col, grid, ROWS, COLS)
        
        return 0
    
    def bfs(self, row, col, grid, ROWS, COLS):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(row, col)])
        visited = set()

        visited.add((row, col))
        perimeter = 0

        while queue:
            x, y = queue.popleft()
            for directionX, directionY in directions:
                newX, newY = x + directionX, y + directionY
                if newX < 0 or newX == ROWS or newY < 0 or newY == COLS or grid[newX][newY] == 0:
                    perimeter += 1
                elif (newX, newY) not in visited:
                    visited.add((newX, newY))
                    queue.append((newX, newY))
        return perimeter