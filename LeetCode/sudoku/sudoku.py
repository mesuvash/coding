class Sudoku:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.

    def solveSudoku(self, board):

        def isSafe(rid, colid):
            # check row/clolumn
            value = board[rid][colid]
            for i in range(len(board)):
                if (board[i][colid] == value) and (i != rid):
                    return False
                if (board[rid][i] == value) and (i != colid):
                    return False

            # check local block
            block_size = int(len(board) ** (0.5))
            block_col = colid // block_size
            block_row = rid // block_size
            for r in range(block_size * block_row, block_size * (block_row + 1)):
                for c in range(block_size * block_col, block_size * (block_col + 1)):
                    if ((board[r][c] == value) and (r != rid) and (c != colid)):
                        return False
            return True

        def solve(row_idx, col_idx):
            if row_idx >= len(board):
                return True

            if col_idx >= (len(board) - 1):
                next_col_idx = 0
                next_row_idx = row_idx + 1
            else:
                next_row_idx = row_idx
                next_col_idx = col_idx + 1

            if board[row_idx][col_idx] == ".":
                for j in range(1, 10):
                    board[row_idx][col_idx] = str(j)
                    if isSafe(row_idx, col_idx):
                        if solve(next_row_idx, next_col_idx):
                            return True
                    board[row_idx][col_idx] = "."
            else:
                if solve(next_row_idx, next_col_idx):
                    return True
            return False
        solve(0, 0)


if __name__ == '__main__':
    sudoku = Sudoku()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    sudoku.solveSudoku(board)
    for i in board:
        print i
