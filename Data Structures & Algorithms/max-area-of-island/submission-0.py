class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        maxArea = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, self.bfs(row, col, ROWS, COLS, grid))
        
        return maxArea

    def bfs(self, row, col, ROWS, COLS, grid) -> int:
        visited = {(row, col)}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(row, col)])

        area = 1
        while queue:
            x, y = queue.popleft()
            for directionX, directionY in directions:
                newX, newY = x + directionX, y + directionY
                if ((newX, newY) in visited or newX < 0 or newX == ROWS or newY < 0 or
                 newY == COLS or grid[newX][newY] == 0):
                 continue
                area += 1
                queue.append((newX, newY))
                visited.add((newX, newY))
        
        return area