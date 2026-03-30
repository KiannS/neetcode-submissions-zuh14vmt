class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridMap = defaultdict(set)
        rows = len(board)
        cols = len(board[0])
        colMap = defaultdict(set)
        
        
        for i in range(rows):
            rowSet = set()
            for j in range(cols):
                if board[i][j] =='.':
                    continue
                # check row
                if board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
                #check col
                if  board[i][j] in colMap[j]:
                    return False
                colMap[j].add(board[i][j])
                #check grid
                grid = (i//3, j//3)
                if board[i][j] in gridMap[grid]:
                    return False
                gridMap[grid].add(board[i][j])
        return True
                
                