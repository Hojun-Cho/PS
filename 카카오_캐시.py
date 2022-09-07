from collections import deque
from typing import List

def solution(cacheSize: int, cities: List[str])-> int:
    answer = 0 
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.upper()
        if city in cache :
            cache.remove(city)
            cache.append(city)
            answer +=1
        else :
            cache.append(city)
            answer+=5
    return answer 
  
  from typing import List


def solution(cacheSize: int, cities: List[str])-> int:
    if cacheSize == 0 :
        return len(cities)*5
    answer = 0
    size = 0 
    cache: dict[str,int]= {}
    for i,city in enumerate(cities) :
        city = city.upper()
        if cache.get(city) != None:
            cache[city] = i   
            answer +=1
        elif size < cacheSize:
            cache[city] = i
            size +=1 
            answer +=5 
        else :
            lru = min(cache,key = cache.get)
            del cache[lru]
            cache[city] = i
            answer +=5 
    return answer
