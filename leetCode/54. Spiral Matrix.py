class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix),len(matrix[0])
        i = j =count = 0 
        answer = [-101] *(n*m)
        while True :
            for k in range(m):
                answer[count] = matrix[i][j]
                j,count = j+1,count+1
            i,j = i+1,j-1
            n,m = n-1,m-1
        
            for k in range(n):
                answer[count] = matrix[i][j]
                i,count = i+1,count+1 
            if answer[-1] != -101 : return answer
            i,j = i-1,j-1
            n-=1 
            
            for k in range(m):
                answer[count] = matrix[i][j]
                j,count=j-1,count+1
            if answer[-1] != -101 : return answer
            i,j =  i-1,j+1
            m-=1
            
            for k in range(n):
                answer[count] = matrix[i][j]
                i,count = i-1,count+1
            if answer[-1] != -101 : return answer
            i,j = i+1,j+1
        return answer
            
        
