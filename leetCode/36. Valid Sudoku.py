class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.isValidcol(board) or not self.isValidRaw(board) :
            return False 
        for i in [0,3,6] :
            for j in [0,3,6]:
                used = [False] * 10 
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] != "." :
                            if used[int(board[i+x][j+y])] :
                                return False 
                            used[int(board[i+x][j+y])]=True
        return True 
                        
    def isValidcol(self,board:List[List[str]]):
        for i in range(9):
            used = [False] * 10 
            for j in range(9):
                if board[i][j] != "." :
                    if used[int(board[i][j])] :
                        return False
                    used[int(board[i][j])] = True 
        return True
                
    def isValidRaw(self,board:List[List[str]]):
        for i in range(9):
            used = [False] * 10 
            for j in range(9):
                if board[j][i] != ".":
                    if used[int(board[j][i])]:
                        return  False
                    used[int(board[j][i])]=True
        return True 

            
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    idx = (i//3) * 3 + j//3 
                    if num in row[j] or num in col[i] or num in box[idx]:
                        return False 
                    col[i].add(num)
                    row[j].add(num)
                    box[idx].add(num)
        return True 
                    
                        
                    
                        
        
                
                    
                        
                    
                        
        
