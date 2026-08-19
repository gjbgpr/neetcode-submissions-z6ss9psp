class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        squares = defaultdict(set)
        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col].isnumeric():
                    num = board[row][col]
                    if (num in rows_dict[row] or 
                    num in cols_dict[col] or 
                    num in squares[(row//3, col // 3)]):
                        return False
                    rows_dict[row].add(num)
                    cols_dict[col].add(num)
                    squares[(row // 3, col // 3)].add(num)
        return True