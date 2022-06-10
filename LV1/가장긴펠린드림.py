### 투포인터  (0,1) (0,2) ->  (1,2) , (1,3) -> (2,3) , (2,4) 
def check(left,right,length,s):
    while left >=0 and right <length and s[left] == s[right] :
        left -=1
        right +=1 
    return right - (left+1)
def invoke(i,length,s):
    return max(check(i,i+1,length,s),check(i,i+2,length,s))
def solution(s):
    length = len(s)
    if length == 1 or s == s[::-1] :
        return length 
    return max([ invoke(i,length,s) for i in range(length-1)])
