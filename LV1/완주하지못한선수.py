def solution(participant, completion):
    answer = ''
    dic = {}
    for x in participant:
        if not dic.get(x) :
            dic[x] =1 
        else :
            dic[x]+=1 
    for x in completion:
        dic[x] -=1 
    for x in dic.keys():
        if dic[x] > 0 :
            return x 
    return answer
