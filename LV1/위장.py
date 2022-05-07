
def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes :
        if dic.get(c[1]) : 
            dic[c[1]]+=1 
        else :
            dic[c[1]]= 1
    print(dic)
    for item in sorted(dic.values()) :
        answer*=(item+1)
    return answer -1 