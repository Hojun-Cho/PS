board = [] 
def solution(rows, columns, queries):
    global board 
    board = [[0]*columns for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = count 
            count +=1 
    return [ rotate(query) for query in queries]
    
    
def rotate(q):
    global board 
    r1,c1,r2,c2 = q[0] -1 ,q[1] -1,q[2]-1,q[3]-1
    answer = board[r1][c1]
    temp = board[r1][c1]
    for r in range(r1,r2):
        board[r][c1] = board[r+1][c1] 
        answer = min(answer,board[r][c1] )
    for c in range(c1,c2):
        board[r2][c]=board[r2][c+1]
        answer = min(answer,board[r2][c] )
    for r in range(r2,r1,-1):
        board[r][c2] = board[r-1][c2] 
        answer = min(answer,board[r][c2] )
    for c in range(c2,c1,-1):
        board[r1][c] = board[r1][c-1] 
        answer = min(answer,board[r1][c] )
        
    board[r1][c1+1] = temp 
    return answer 
