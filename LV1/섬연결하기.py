# break를 추가하는 이유 => 
# 1-4 : 1 , 0 ->3 : 2 , 1->2 :2 , 0->4 :3 , 2->5 :3 ,5-> 4 : 4, 1->0 : 5
# 1에서 출발하면 0->3을 건너뛴다. 왜냐하면 set안에 0,3이라는 정점이 모두 포함되지 않아서!! 
# 따라서 아예 새로운 정점이 추가된 경우 기존에 set에 포함시키지 못한 간선을 다시 봐줘야 한다. 


from collections import *
import sys
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) 
    connect = set([costs[0][0]]) # 연결을 확인하는 집합
    
    while len(connect) < n :
        for cost in costs :
            # 사이클이 존재하는지 확인
            if cost[0]  in connect  and cost[1] in connect :
                continue 
            # 아직 존재하지 않는 간선이라면 최소간선인 따라서 set을 업데이트한다
            if cost[0] in connect or cost[1] in connect : 
                connect.update([cost[0],cost[1]])
                answer+=cost[2]
                break
    return answer
