import collections 

        
def solution(cacheSize, cities):
    answer = 0
    stack= collections.deque()
    _len = 0
    dic ={} 
    if cacheSize == 0 :
        return 5 * len(cities)
    
    for city in cities:
        city= city.upper();
        if dic.get(city) and dic[city] == 1 :
            # 캐시에 들어있다는 의미 
            # 현재 값을 가장 앞에 둬야함 
                answer +=1 
                stack.remove(city)
                stack.appendleft(city)
        else : #아직 등록된 도시가 아닌경우, 캐시에 없는 경우 
            if cacheSize <= _len :  # 캐시가 꽉 찬경우 
                dic[stack.pop()] = 0 # 가장 마지막에 참조된 놈을 팝한다,캐시에서 지워준다 
                stack.appendleft(city) # 현재 놈을 맨 앞에 넣는다
            else : # 캐시가 꽉 차지 않은경우 
                stack.appendleft(city)
                _len +=1 
            answer +=5 # 캐시 미스 
            dic[city] =1 
 
    return answer

## 깔끔한 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    answer  = 0
    for city in cities :
        city =  city.upper() 
        if city in cache :
            answer +=1 
            cache.remove(city)
            cache.append(city)
        else :
            answer +=5
            cache.append(city) 
    return answer 
            
            
