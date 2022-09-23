from collections import defaultdict, deque
from math import inf
from typing import List
N = 0 
Map = defaultdict(list)
Summits = {}
# distance = summit까지 가장 오래 걸리는 시간
# answer : summit 의 intensity가 가장 짧은 시간
def solution(n, paths, gates, summits) -> List[int]:
    global Map,N,Summits
    N = n
    Summits = dict.fromkeys(summits,True)
    min_dis = inf
    min_sum = -1 
    answer = []
    for path in paths :
        Map[path[0]].append([path[1],path[2]])
        Map[path[1]].append([path[0],path[2]])
    
    dis =  [inf if i not in gates else 0 for i in range(n+1)]
    dis = find_max(gates,dis)
    
    # summits에서 최소 summit를 찾는다 
    for summit in summits:
        if min_dis > dis[summit]:
            min_dis = dis[summit] 
            min_sum = summit 
        elif min_dis == dis[summit] :
            min_sum = min(min_sum,summit)
    return [min_sum,min_dis]
    
            
            
def find_max(gates,distance):
    global Map,N,Gates,Summits
    
    q = deque(gates)
    while q :
        now = q.popleft()
        if Summits.get(now) != None :
            continue
        for next,cost in Map[now]:
            if distance[next] > max(distance[now],cost) :
                q.append(next)
                distance[next] = max(distance[now],cost)
    return distance
