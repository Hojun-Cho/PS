# O(n*m^2)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        last_zeros = [False]*len(matrix[0])
        for i,col in enumerate(matrix) :
            zero = -1 
            for j,num in enumerate(col) :
                if num == 0 :
                    for k in range(i):
                        matrix[k][j] = 0 
                    last_zeros[j] = True
                    matrix[i][j] = 0  
                    zero = j if zero == -1 else zero 
                elif num != 0 and zero != -1 :
                    matrix[i][j] = 0 
                if last_zeros[j] :
                    matrix[i][j] = 0
            for k in range(zero) :
                matrix[i][k] = 0 
                
                
# 매번 행,열을 확인하며 0으로 바꿔줄 필요가 없다
# O(n-1 * m-1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len,col_len = len(matrix),len(matrix[0])
        # row,col 의 첫 행, 첫 열 중에서 0가 있는지 확인한다. 있다면 체크
        is_zero_row = False 
        for r in range(row_len):
            if matrix[r][0] == 0 :
                is_zero_row = True 
                break 
        is_zero_col = True if matrix[0].count(0) else False 

        # 현재 위치가 0 : 첫 열,첫 행을 0으로 체크한다
        for r in range(1,row_len):
            for c in range(1,col_len):
                if matrix[r][c] == 0 :
                    matrix[r][0],matrix[0][c] = 0,0 
        
        # 현재 row또는 col에 0이 들어있는지 확인한다. 있다면 0으로 설정
        for r in range(1,row_len):
            for c in range(1,col_len):
                 if matrix[r][0] == 0 or matrix[0][c] == 0 :
                    matrix[r][c] = 0 
        # 지금까지 1열과 1행은 확인하지 않았음, 1행과 1열을 제외하고는 모두 값이 설정되었기 때문에 1열과 1행만 살펴본다.
        if is_zero_row :
            for r in range(row_len):
                matrix[r][0] = 0
        if is_zero_col:
            for c in range(col_len):
                matrix[0][c] = 0 
           
