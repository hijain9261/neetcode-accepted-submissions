class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue

                row_token = f"r{r}-{value}"
                col_token = f"c{c}-{value}"
                box_token = f"r{r//3}&c{c//3}-{value}"

                if row_token in seen or col_token in seen or box_token in seen:
                    return False
                seen.add(row_token)
                seen.add(col_token)
                seen.add(box_token)
        return True

                
