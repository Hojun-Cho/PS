from collections import defaultdict
import math


def solution(fees, records):
    answer = []
    cars ={}
    costs = defaultdict(int) 
    for fee in records:
        time,num,inout=fee.split(" ")
        h,m = time.split(":")
        time = int(h) * 60  + int(m)
        if num in cars :
            costs[num] += time - cars[num] 
            del cars[num]
        else :
            cars[num] =time 
    end = int(23) * 60 + 59
    for key,val in cars.items() :
        costs[key] += end - val 
     
    fees = [int(fee) for fee in fees]
    answer = defaultdict(int)
    for key,cost in costs.items() :
        if cost <= fees[0]:
            answer[int(key)] = fees[1] 
        else :
            answer[int(key)] = fees[1] +(( math.ceil((cost - fees[0])/fees[2]) *fees[3]))
    return [val[1] for val in sorted(answer.items())]
    
import re 
import math
def solution(fees, records):
    answer = []
    dic = {} 
    for record in records :
        result =re.split(r"([:|\s])",record)
        if dic.get(result[4]): 
            dic[result[4]].append( int(result[0])* 60 + int(result[2]))
        else :
            dic[result[4]]= [ int(result[0])* 60 + int(result[2]) ]
    maxTime = 23* 60 + 59
    answer = [] 
    sorted(dic.keys())
    for key in sorted(dic.keys()):
        result = [] 
        times = dic.get(key)
        if len(times ) %2 !=0 :
            times.append(maxTime)
        last = 0 
        for i in range(0,len(times),2):
            result.append(times[i+1]-times[i])
        result = sum(result)
        if result <= fees[0]  :
            answer.append(fees[1])
        else : 
            answer.append( fees[1] +math.ceil(( result- fees[0])/fees[2]) * fees[3])
    return answer
