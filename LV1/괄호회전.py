import collections
def isCorrect(s):
    stack = []
    _len = 0
    for x in s :
        if  x == "[" or x== "{" or x == "(" :
            stack.append(x) 
            _len +=1 
        elif _len >0 :
            if stack[-1] == "[" and x == "]":
                stack.pop()
                _len -=1
            elif stack[-1] == "(" and x == ")":
                stack.pop()
                _len -=1 
            elif stack[-1] =="{" and x== "}":
                stack.pop()
                _len-=1
        else :
            return False
    return True if _len == 0 else False
def solution(s):
    answer = 0
    q = collections.deque(s)
    for i in range(len(s)):
        if isCorrect(q) : 
            answer+=1 
        q.append(q.popleft())
    return answer

solution("[](){}")
