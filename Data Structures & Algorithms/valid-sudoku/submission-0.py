class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = {}
        for i in range(0,9):
            for j in range(0,9):
                val = board[i][j]
                square_set = (i//3, j//3)
                if val in rows[i] or val in cols[j]:
                    return False
                if square_set not in box:
                    box[square_set] = set()
                if val in box[square_set]:
                    return False
                if val != '.':
                    rows[i].add(val)
                    cols[j].add(val)
                    box[square_set].add(val)
        
        return True

        

        