# input이 0 < orders <= 10 
# 0< course <= 10 
# 조합을 이용해도 충분한 범위
from itertools import combinations
from typing import Counter


def solution(orders, course):
    counter = Counter()
    for order in orders :
        counter.update(order)
    safe_menu = {}
    for k,v in counter.items():
        if v > 1 :
            safe_menu[k] = True 
    for i,order in enumerate(orders):
        temp = [o for o in order if safe_menu.get(o) != None]
        temp.sort()
        orders[i] = temp
        
    answer = [] 
    for c in course :
        combi_arr = [] 
        for order in orders :
           combi_arr += list(combinations(order,c))
        counter = Counter(combi_arr)
        answer += [''.join(k) for k,v in counter.items() if max(counter.values()) == v and v >1 ] 
        
    return sorted(answer )
