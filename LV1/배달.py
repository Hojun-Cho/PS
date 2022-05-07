def solution(N, road, K):
    dic = {}
    stack = [[1,1,0]]   
    cost = [[500001] *(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        dic[i] = []

    for t in road :
        if t[0] == 1 :
            stack.append([1,t[1],t[2]]) 
        
        dic[t[0]].append([t[1],t[2]] ) # 출발지에서 가는 경우의 수 
        dic[t[1]].append([t[0],t[2]])
    answer = []
    # 시작은 항상 1에서 
    
    while stack :
        last,i,n = stack.pop() #출발지 , 현재 위치 ,현재 위치에 도달하기 까지 비용 
        if n> K :
            continue 
        elif n <= K : 
            answer.append(i) #도착지를 정답에 넣는다 
            for item in dic[i] :  
                if  n+item[1] <=K and   item[1] + n <=cost[i][item[0]]  :  
                    cost[i][item[0]] = item[1] + n 
                    stack.append([i,item[0] ,item[1] + n])  #출발지 ,도착지

            
                
    return len(set(answer))

# print(solution(5	,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	,3))
