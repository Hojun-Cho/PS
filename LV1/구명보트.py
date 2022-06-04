# 투포인터를 활용하자 
# 제일 가벼운 사람과 제일 무거운 사람이 같이 타는 경우 limit 보다 크다면 제일 무거운 사람은 어느 누구와도 같이 타는게 불가능하다
# 따라서 제일 무거운 사람은 혼자 타야 하므로 answer +=1 이 된다
# 만약 길이가 1이면 남은 사람이 혼자 타니깐 +1 하고 break
# 제일 가벼운 사람과 제일 무거운 사람이 같이 탈 수 있는 경우 둘 다 pop 해준다 
# ######################################### 
# 주의사항 # 
# 순차적으로 접근한다면 최적의 답이 나오지 않는다
# 1 2 3 4 5 5  이고 limit이 6인 경우 
# 1 + 2 => 1
# 3 => 2 
# 4 => 3 
# 5 => 4
# 5 => 5 로서 총 5번 배가 이동한다 
# 1 + 5  => 1 
# 5 => 2
# 2 + 4 => 3
# 3  => 4  로서 총 4번의 배가 이동한다 
#따라서 순차적인 접근으로는 최적의 답이 나오지 않는다 
from collections import deque 
def solution(peoples, limit):
    answer = 0
    peoples = deque(sorted(peoples))
    deq = deque()
    while peoples : 
        if len(peoples) == 1 :
            answer +=1 
            break 
        if peoples[0] + peoples[-1] <= limit :
            peoples.pop()
            peoples.popleft()
        elif peoples[0] + peoples[-1] > limit :
            peoples.pop()
        answer +=1 
    return answer 
