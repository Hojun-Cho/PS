import sys

def solution(s):
    answer = sys.maxsize
    length = len(s)
    for i in range(1,length+1):
        answer = min(answer,zip(s,length,i))
    return answer
# count 단위로 압축
def zip(s: str,length: int,size: int) -> int:
    last = s[:size]
    i = 0 
    count = 0 
    answer= 0 
    for i in range(0,length +size ,size):
        now = s[i:i+size] 
        if last == now:
            count +=1                 
        else :
            if count > 1 :
                answer += len(str(count)) + len(last)
            else :
                answer += len(last)
            count = 1 
            last = now 
    return answer 
    

                
