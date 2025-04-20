from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Helper function to try placing queens row by row
        def backtrack(row: int, diagonals: set, anti_diagonals: set, cols: set, state: List[int]):
            # Base case: All queens are placed
            if row == n:
                # Convert column positions in `state` to a board configuration
                board = []
                for i in state:
                    row_repr = ['.'] * n  # Create an empty row
                    row_repr[i] = 'Q'     # Place queen at the correct column
                    board.append("".join(row_repr))
                solutions.append(board)  # Save this valid board
                return
            
            # Try placing queen in each column of the current row
            for col in range(n):
                diag = row - col             # Main diagonal identifier
                anti_diag = row + col        # Anti-diagonal identifier

                # If this column or diagonal is already attacked, skip it
                if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                    continue

                # Choose: Place the queen and mark the column and diagonals
                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)
                state.append(col)

                # Explore: Move to the next row
                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                # Unchoose: Remove the queen and backtrack
                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)
                state.pop()

        solutions = []  # Holds all the valid board configurations
        backtrack(0, set(), set(), set(), [])  # Start from the first row
        return solutions  # Return all possible solutions

def test_n_queens():
    solver = Solution()
    
    # Test case 1: n = 1
    assert solver.solveNQueens(1) == [["Q"]]

    # Test case 2: n = 4
    result = solver.solveNQueens(4)
    expected = [
        [".Q..","...Q","Q...","..Q."],
        ["..Q.","Q...","...Q",".Q.."]
    ]
    assert sorted(result) == sorted(expected)

    # Test case 3: n = 5 (only checking length due to many possible valid outputs)
    result_5 = solver.solveNQueens(5)
    assert len(result_5) == 10  # There are 10 valid configurations for n = 5

    print("All test cases passed!")

test_n_queens()
