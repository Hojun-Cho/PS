# https://programmers.co.kr/learn/courses/30/lessons/64065
import collections
def solution(s):
    dic = {}
    count=0
    temp=[]
    answer=[]
    long =''
    s = collections.deque(s)
    s.popleft()
    s.pop()
    while s:
        x=s.popleft()
        if x == "{":
            while True:
                x =s.popleft()
                if x == "}":
                    temp.append(int(long))
                    dic[count] = temp
                    temp=[]
                    count =0
                    long =''
                    break
                elif x == "," :
                    temp.append(int(long))
                    count +=1
                    long=''
                
                
                else :
                    long+=x
        
        
    
    keys =sorted(dic.keys())
    for key in keys:
        if key=="0":
            continue 
        for k in dic[key] :
            if int(k) not in answer:
                answer.append(int(k))
        
        
        
            
        
        
        
        
        
    

    return answer
