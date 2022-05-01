# https://programmers.co.kr/learn/courses/30/lessons/64065
import collections
def solution(s):
    dic = {}
    s = collections.deque(list(s))
    answer = [] 
    while s :
        temp = []
        if s[0] == "{":
            while s and  s[0] !="}" :
                temp.append(s.popleft())
        if s and s[0] == "}" :
            s.popleft()
        # answer.append(temp)
    

    return answer