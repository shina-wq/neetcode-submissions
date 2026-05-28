class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track seen numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                # Skip empty cells
                if value == ".":
                    continue

                # Determine which 3x3 box the cell belongs to
                box_index = (r // 3) * 3 + (c // 3)

                # Check for duplicates
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in boxes[box_index]
                ):
                    return False

                # Add value to tracking sets
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)

        return True