from collections import deque
X= [1,0,-1,0]
Y= [0,1,0,-1]
def valid_point(x,y,z):
    return 0<=x+X[z]<5 and  0<=y+Y[z]<5
def valid(place):
    visit =[ [False]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            # P인경우만 시작하자 ! 
            if not visit[i][j] and place[i][j] == "P":
                stack = deque()
                stack.append([i,j,0])
                #P는 방문체크 하면 안된다 
                visit[i][j] = True if place[i][j] != "P" else False
                while stack: 
                    x,y,dis = stack.popleft()
                    #시작과 같으면 노노 
                    if (x != i or y != j) and place[x][y]=="P" :
                        if 0< dis <= 2 :
                            return 0
                        else :
                            continue# 다음번 P에게 맞기고 나는 떠나자 
                    for z in range(4):
                        if  valid_point(x,y,z) and  not visit[x+X[z]][y+Y[z]]:     
                            visit[x+X[z]][y+Y[z]]  =True if  place[x+X[z]][y+Y[z]] != "P" else False

                            if place[x+X[z]][y+Y[z]] != "X" :
                                stack.append([ x+X[z],y+Y[z],dis+1])                   
    return 1  
def solution(places):
    answer = []
    for place in places :
        answer.append(valid(place))       
    return answer
    

# No.	0	1	2	3	4
# 0	    P	O	O	P	X
# 1	    O	X	P	X	P
# 2 	P	X	X	X	O
# 3	    O	X	X	X	O
# 4	    O	O	O	P	P

# 1. (1,4)에서 (4,4)에 접근하고 visit 체크를 한다면 (4,3)에서 (4,4)ㅇ에 접근할 수 없음
# 2. (2,0)에서 방(4,3)에 접근하고 visit 체크를 한다면 (4,3)에서 (4,4)에 접근할 수 없음 
# 결론 => p에는 방문체크를 하지 말자 
