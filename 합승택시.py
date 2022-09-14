from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import Dict, List

# bfs를 이용하려면 visited 체크가 필요하다
def bfs(n,start: int,end: int,fares: Dict[int,List[int]] ):
    deq =[[0,start]] 
    costs = [ inf if i!= start else 0 for i in range(n+1) ]
    while deq :
        currCost,curr = heappop(deq)
        if currCost > costs[curr]:
            continue 
        for f in fares[curr] : 
            if f[1] + currCost < costs[f[0]]:
                heappush(deq,[f[1] + currCost,f[0]])
                costs[f[0]]=f[1]+currCost
    return costs[end]
def solution(n: int, s: int , a: int, b: int, fares:List[List[int]]):
    paths :Dict[int,List[int]] = defaultdict(list)
    for path in fares:
        paths[path[0]].append(path[1:])
        paths[path[1]].append([path[0],path[2]])
    answer = inf
    for i in range(1,n+1): 
        s_t = bfs(n,s,i,paths) 
        t_a = bfs(n,i,a,paths)
        t_b = bfs(n,i,b,paths)
        answer = min(s_t+t_a+t_b,answer)
    return answer 
