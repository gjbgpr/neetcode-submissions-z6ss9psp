class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        fresh = 0
        time = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                    
                for directionX, directionY in directions:
                    newX, newY = x + directionX, y + directionY
                    if ((newX,newY) in visited or newX < 0 or newX == ROWS or newY < 0 or 
                    newY == COLS or grid[newX][newY] == 0 or grid[newX][newY] == 2):
                        continue
                    queue.append((newX, newY))
                    visited.add((newX, newY))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1