##내 풀이
def solution(id_list, report, k):
    users = {} #신고한 사람
    count = {} #신고당한수 , 나를 신고한 사람 수
    answer = [0]*len(id_list)
    for i,name in enumerate(id_list):
        count [name] = [0,0] 
        users[name] = {}
        
    for i in range(0,len(report)):
        user,ban = report[i].split()
        if not users[user].get(ban) :
            count[ban]=[count[ban][0]+1,count[ban][1] +1] 
            users[user][ban]=1
     
    for i,id in enumerate(id_list) :
        for name in users[id] :
            if count[name][0] >= k :
                answer[i] += 1 
    return answer


### 깔끔한 풀이
def solution(id_list, report, k):
    count = {} #신고당한 사람 이름,신고당한 수 
    answer = [0]*len(id_list)
    
    for users in set(report):
        a,b = users.split()
        count[b] = (count[b] +1) if  count.get(b) else 1
        
    for r in set(report) : 
        if count[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] +=1 
            
    return answer


