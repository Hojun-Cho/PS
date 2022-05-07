# 송전탑의 개수가 비슷하다는 것은 차이가 최소라는 뜻
# 한 정점에서 연결된 다른 정점의 수를 구한다
# 인접 리스트 
def bfs(board,visited,start):
    stack = [start]
    result = 1 # 현재 시작점은 송전탑에 연결되었다고 생각
    visited[start] = True # 현재 시작점은 이미 방문 완료 
    while stack : 
        now = stack.pop()
        for x in board[now] :
            if not visited[x]  : #연결된 송전탑중 아직 방문 x
                result +=1 
                stack.append(x)
                visited[x] = True 
    return result 
    
    
# 하나씩 연결을 끊어서 생각한다
def solution(n, wires):
    board= [[] for _ in range(n)]
    answer =101
    for x,y in wires:
        board[x-1].append(y-1)
        board[y-1].append(x-1)
        
    for start,not_visit in wires:
        start-=1 
        not_visit -=1  
        
        visited= [False]*n
        visited[not_visit] = True  # 이 경로는 끊어진 경로 
        result  = bfs(board,visited,start)
        answer = min(abs (result-(n-result)),answer)
        if answer == 0: 
            break;
        
    return answer



# 더 느린 방법 
# 인접 행렬  , 방문 체크가 추가로 필요하다 
# def solution(n, wires):
#     answer = 101
#     def bfs(board,start,end):
#         visited=[False]*n
#         visited[start] =True 
#         visited[end]=True 
#         result =1  # 현재 위치한 송전탑의 수를 더한다 
#         stack = [start]
        
#         while stack :
#             now = stack.pop()
#             for i in range(n):
#                 if board[now][i] and not visited[i] :
#                     stack.append(i)
#                     result +=1 
#                     visited[i] =True 
#         return result 

#     board= [[0]*n  for _ in range(n)]
#     for x,y in wires :
#         board[x-1][y-1] = 1
#         board[y-1][x-1] = 1 
    
#     for start,end in wires :
#         board[start-1][end-1] = 0 
#         board[end-1][start-1] = 0
#         result = bfs(board,start-1,end-1)
#         board[start-1][end-1] = 1 
#         board[end-1][start-1] = 1
#         print(result)
#         answer = min(answer,abs(result-(n-result)))
        
        
#     return answer