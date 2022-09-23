from collections import deque

def solution(places) -> List[bool]:
    answer = []
    return [ 1 if find(p) else 0 for p in  places ]
  
def find(places) -> bool:
    for r in range(5):
        for c in range(5):
            if places[r][c] == 'P' and dfs(places,r,c):
                return False  
    return True 
               
def dfs(places,r,c) -> bool:
    q = deque() 
    visited = [ [False] * 5 for _ in range(5)]
    q.append([r,c])
    while q :
        x,y = q.popleft()
        if visited[x][y] : 
            continue
        visited[x][y] = True 
        if (x!= r or y != c) and  places[x][y] == 'P' :
            return True 
        if abs(x+1-r) + abs(y-c) <= 2 and x+1 < 5 and places[x+1][y] !='X':
            q.append([x+1,y])
        if abs(x-1-r) + abs(y-c) <= 2 and 0<= x-1  and places[x-1][y] !='X':
            q.append([x-1,y])
        if abs(x-r) + abs(y+1-c) <= 2 and y+1 < 5 and places[x][y+1] !='X':
            q.append([x,y+1])
        if abs(x-r) + abs(y-1-c) <= 2 and 0<= y-1  and places[x][y-1] !='X':
            q.append([x,y-1])
    return False 

    

    
