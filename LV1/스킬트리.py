from collections import deque
def solution(skill, skill_trees):
    answer = len(skill_trees)
    dic = {} 
    for s in skill : 
        dic[s] = True 

    for skills in skill_trees :
        learn = deque(skill) 
        for s in skills : 
            if dic.get(s) :
                if learn[0] == s : 
                    learn.popleft()
                else :
                    answer -=1 
                    break
    return answer
