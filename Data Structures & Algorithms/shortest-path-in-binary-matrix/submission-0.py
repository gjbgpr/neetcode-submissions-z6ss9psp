class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return  -1
        
        directions = {(1,0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)}

        distance = 1
        queue = deque([(0,0)])
        visited = {(0,0)}
        while queue:
            current_distance = len(queue)
            for _ in range(current_distance):
                row, col = queue.popleft()
                if (row, col) == (ROWS - 1, COLS - 1):
                    return distance
                for directionX, directionY in directions:
                    newX, newY = row + directionX, col + directionY
                    if ((newX, newY) in visited or newX < 0 or newX == ROWS or 
                    newY < 0 or newY == COLS or grid[newX][newY] == 1):
                        continue
                    visited.add((newX, newY))
                    queue.append((newX, newY))
            distance += 1
        return -1