# deque가 아닌 다른 풀이로도 꼭 풀어보자 
import collections 
def solution(s):
    answer  ,length = 1001,len(s)
    if length == 1 :
        return 1 
    for i in range(1,length//2+1)  :
        result = collections.deque([ s[j:j+i] for j in range(0,length,i)])
        tempAnswer = ''
        last = result[0]
        rept = 0
        while result :
            now  = result.popleft()
            if now == last : 
                rept +=1
            elif now != last :
                tempAnswer += (str(rept)+last) if rept > 1 else last 
                rept = 1 
                last = now      
            if not result : 
                tempAnswer += (str(rept) + last) if rept > 1 else last
        answer = min(len(tempAnswer),answer)
    return answer


### 소소한 재미. . .
import collections 
def solution(s):
    answer  ,length = 1001,len(s)
    if length == 1 : return 1 
    results = []
    [results.append( collections.deque([ s[j:j+i] for j in range(0,length,i)])) for i in range(1,length//2 +1)]
    for result in results :
        last ,rept ,tempAnswer= result[0] , 0 , ''
        while result :
            now  = result.popleft()
            rept +=1 if now == last else 0
            if now != last :
                tempAnswer += (str(rept)+last) if rept > 1 else last 
                rept = 1 
                last = now      
            if not result : tempAnswer += (str(rept) + last) if rept > 1 else last
        answer = min(len(tempAnswer),answer)
    return answer
