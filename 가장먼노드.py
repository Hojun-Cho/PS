import sys
from collections import defaultdict
from collections import deque
def solution(n, edge):
    ### 각각의 최단경로를구한다
    graph = defaultdict(list)
    visit = [False for i in range(n)]
    costs = [ sys.maxsize for i in range(n) ]
    visit[0]=True 
    for start,end in edge :
        graph[start-1].append(end-1)
        graph[end-1].append(start-1)
    q = deque([[0,0]])
    while q :
        now,cost = q.popleft()
        costs[now] = min(costs[now],cost) 
        # visit[now]=True  여기서 방문체크하면 시간초과 ! 이유는 최단거리가 아닌 거리를 방문하기 때문에
        for _next in graph[now] :
            if not  visit[_next] and costs[_next] > cost+1:
                visit[_next]=True  # 만약 for문 밖에서 방문체크를 한다면 1=>2=>4=>3 으로 방문하는 경로가 존재한다. 하지만 이 경로는 최단 경로가 아니다. 따라서 for문 안에서 방문체크!! 
                q.append([_next,cost+1])
                
    return costs.count(max(costs))
