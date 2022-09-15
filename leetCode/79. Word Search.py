from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        target = len(word)
        n , m = len(board),len(board[0])
        n_x ,n_y = [0,0,1,-1] , [1,-1,0,0]

        def dfs(x,y,index) -> bool :
            if index >= target :
                return True 
            if x <0 or x>= n or y <0 or y >= m or word[index] != board[x][y]:
                return False 
            
            board[x][y] ,tmp = "%",board[x][y] 
            for i in range(4):
                if dfs(x+n_x[i],y+n_y[i],index+1) :
                    return True 
            board[x][y] = tmp
            return False
                
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0) :
                    return True
        return False 
