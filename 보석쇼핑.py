# 처음에 defaultdict(bool)로 접근했다. 하지만 '모든 '보석을 소지하는게 정답이라서 int로 변경했다
from collections import defaultdict
def solution(gems):
    gems_count = len(gems)
    jems_kind = len(set(gems))
    answer = []
    have = defaultdict(int)
    start = end =  0
    answer = [100000,0]
    while end <= gems_count  :
        if have["###"] == jems_kind :
            answer = [start,end] if  abs(answer[0]-answer[1])> abs(start-end) else  answer 
            have[gems[start]] -= 1 
            if have[gems[start]] <= 0 :
                del have[gems[start]] 
                have["###"] -=1 
            start +=1 
        elif have["###"] != jems_kind :
            if end < gems_count : 
                have[gems[end]] +=1 
                have["###"] +=1 if have[gems[end]] == 1 else 0 
            end +=1 
    return  [ answer[0]+1,answer[1]]
