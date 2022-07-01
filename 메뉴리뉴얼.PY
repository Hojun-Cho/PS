# 못풀었다... 
# 내일 다시 시도하자!
import itertools
import collections 

def solution(orders, course):
    answer = []
    for c in course :
        dic = collections.defaultdict(int)
        for order in orders : 
            menu = itertools.permutations(order, c)
            for combi in menu :
                dic[''.join(sorted(combi))] +=1
        dic = sorted(dic.items(), key=lambda x: x[1],reverse=True)
        now = 0
        for i,n in enumerate(dic) :
            if n[1] >= now :
                if orders.count(n[0]) < 2 : 
                    continue 
                now = n[1]
                answer.append(n[0])
            else : 
                break

    return answer

### 시간초과 풀이  => 순열을 조합으로 바꾸면 문제가 해결된다 
import itertools
import collections 

def solution(orders, course):
    answer = []
    for c in course :
        dic = collections.defaultdict(int)
        for order in orders : 
            small_dic = collections.defaultdict(int)
            for combi in  itertools.permutations(order, c) :
                result = ''.join(sorted(combi))
                if small_dic[result] == 0 :
                    dic[result] +=1
                    small_dic[result] = 1 
        dic = sorted(dic.items(), key=lambda x: x[1],reverse=True)
        now_count  = 0
        for x in dic : 
            if x[1] >= now_count and x[1] >=2  : 
                now_count= x[1] 
                answer.append(x[0])
            else :
                break
    return sorted(answer)

### 계속 순열로 시도해서 중복이 발생했다 , 조합으로 중복을 제거하자 
import itertools
import collections 

def solution(orders, course):
    answer = []
    for c in course :
        entry = [] 
        for order in orders : 
            for x in itertools.combinations(order,c) : 
                result = ''.join(sorted(x)) 
                entry.append(result) 
        result = collections.Counter(entry).most_common()
        for menu,count in result :
            if count == result[0][1] and count >=2  :
                answer.append(menu)
                now = count 
            else :
                break
    return sorted(answer)
