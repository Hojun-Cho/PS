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
