class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        time = 0

        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    rotten.append((row, col))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh and rotten:
            length = len(rotten)
            for i in range(length):
                row, col = rotten.popleft()

                for direction_row, direction_col in directions:
                    new_row, new_col = row + direction_row, col + direction_col
                    if (new_row in range(ROWS) and
                        new_col in range(COLS) and
                        grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        rotten.append((new_row, new_col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1