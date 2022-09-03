import heapq
from typing import List
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        answer = 0 
        # init
        for u,v,w in times :
            graph[u].append((v,w))
        queue = [[0,k]]
        dist = defaultdict(int)
        
        while queue :
            w,node = heapq.heappop(queue)
            # first visit이 아니며 다 최솟값이 아니다
            if node in dist :
                continue
            dist[node] = w 
            answer = max(answer,w)
            for n_v,n_w in graph[node]:
                if n_v not in dist :
                     heapq.heappush(queue,[n_w+w,n_v])
        return answer if len(dist) == n else -1 
