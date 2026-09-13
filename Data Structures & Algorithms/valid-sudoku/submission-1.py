class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)
        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                val = board[row][col]
                if val != '.':
                    if (val in row_map[row] or 
                    val in col_map[col] or 
                    val in square_map[(row//3, col // 3)]):
                        return False
                    row_map[row].add(val)
                    col_map[col].add(val)
                    square_map[row//3,col//3].add(val)
        
        return True