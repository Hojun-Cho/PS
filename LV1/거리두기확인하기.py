from collections import deque
X= [1,0,-1,0]
Y= [0,1,0,-1]
def is_small_or_like_2(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)  <= 2 

def valid(place):
    visit =[ [False]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if not visit[i][j] and place[i][j] == "P":
                stack = deque()
                stack.append([i,j,0])
                visit[i][j] = True if place[i][j] != "P" else False
                while stack: 
                    x,y,dis = stack.popleft()
                    if (x != i or y != j) and place[x][y]=="P" :
                        if 0< dis <= 2 :
                            return 0;
                        else :
                            continue
                    for z in range(4):
                        if  0<=x+X[z]<5 and  0<=y+Y[z]<5 and  not visit[x+X[z]][y+Y[z]]:     
                            if place[x+X[z]][y+Y[z]] != "P":
                                visit[x+X[z]][y+Y[z]] = True 
                            if place[x+X[z]][y+Y[z]] != "X" :
                                stack.append([ x+X[z],y+Y[z],dis+1])
                                
                                
    return 1 
                    
                
                
def solution(places):
    answer = []

    for place in places :
        answer.append(valid(place))        

            
    
    return answer
