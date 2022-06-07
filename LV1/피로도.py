# 재귀를 이용한 dfs로 쉽게 풀 수 있다.

answer=0
def dfs(depth,k,dungeons,visit):
    global answer 
    for i in range(len(dungeons)) :
        if  not visit[i]  and dungeons[i][0] <= k and dungeons[i][1] <=k: 
            visit[i]=True
            dfs(depth+1,k-dungeons[i][1],dungeons,visit)
            visit[i]=False
    # 정답을 9번 라인에서 처리하면 재귀에서 값이 바뀐다. 즉 MAX값을 저장하지 못한다 
    answer=max(answer,depth)

def solution(k, dungeons):
    visit = [False for _ in range(len(dungeons))]
    dfs(0,k,dungeons,visit)
    return answer 
