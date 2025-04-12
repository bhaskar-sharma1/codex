from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []

        def get_box_index(r, c):
            return (r // 3) * 3 + c // 3

        # Initialize bitmasks
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = int(board[r][c])
                    mask = 1 << val
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[get_box_index(r, c)] |= mask

        def get_candidates(r, c):
            mask = rows[r] | cols[c] | boxes[get_box_index(r, c)]
            return [str(d) for d in range(1, 10) if not (mask & (1 << d))]

        def dfs():
            if not empty_cells:
                return True

            # MRV: pick the cell with the fewest candidates
            min_candidates = 10
            target_idx = -1
            for idx, (r, c) in enumerate(empty_cells):
                candidates = get_candidates(r, c)
                if len(candidates) < min_candidates:
                    min_candidates = len(candidates)
                    target_idx = idx
                if min_candidates == 1:
                    break

            r, c = empty_cells.pop(target_idx)
            for digit in get_candidates(r, c):
                val = int(digit)
                mask = 1 << val

                board[r][c] = digit
                rows[r] |= mask
                cols[c] |= mask
                boxes[get_box_index(r, c)] |= mask

                if dfs():
                    return True

                # Backtrack
                board[r][c] = '.'
                rows[r] ^= mask
                cols[c] ^= mask
                boxes[get_box_index(r, c)] ^= mask

            empty_cells.insert(target_idx, (r, c))
            return False

        dfs()

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

sol = Solution()
sol.solveSudoku(board)

for row in board:
    print(row)
