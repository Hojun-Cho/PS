# 답지봤다.
def solution(n, weak, dist):
    END = len(weak)
    results = [set()]
    dist.sort(reverse=True)
    answer = 0
    
    for can_move in dist : 
        visit = []
        answer +=1 
        # i에서 시작  
        for i,start in enumerate(weak) :
            result = weak[i:] + [n+m for m in weak[:i]]
            can_reach = [e % n for e in result if e - start <= can_move ]
            visit.append(set(can_reach))
        candidate = set()
        for now_list in visit :
            for last_list in results : 
                now = now_list |set(last_list)
                if len(now) == END :
                    return answer
                candidate.add(tuple(now))
        results = candidate
                
    return -1
