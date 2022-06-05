# 어디에 설치할지 
# 몇 대 설치할지
from collections import deque 
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:(x[0],x[1]))
    routes = deque(routes)
    start,end = routes.popleft()
    while routes :
        temp_s ,temp_e = routes.popleft()
        if  start <=temp_s <= end :
            start = temp_s 
            end = min(temp_e,end)
            if not routes :
                answer +=1 
                break
        else : 
            if not routes:
                answer +=2 
                break
            answer +=1 
            start,end = temp_s,temp_e
    return answer
