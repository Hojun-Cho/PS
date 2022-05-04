def split(p):
    left = 0;
    right = 0;
    for  i,x in enumerate(p):
        if  x == "(": 
            left += 1
        else : 
            right += 1
            
        if left == right : # 균형이 맞은 상태
            a = p[:i+1] 
            b = p[i+1:] if i +1 < len(p) else "" 
            break

    return a,b
  
def isCorrect(s):
	stack=[]
	stack.append(s[0])
	for i in range(1,len(s)):
		if len(stack)==0 or stack[-1]==')' or (stack[-1]=='(' and s[i]=='('):
			stack.append(s[i])
		else:
			stack.pop()
	if len(stack)==0: return True
	else: return False
# def isCorrect(p):
#     stack = []
#     length = 0 
#     for x,i in enumerate(p):
#         if x == "(" :
#             stack.append(x)
#             length +=1 
#         elif length > 0 and stack[-1] == "(":
#             stack.pop()
#             length -=1 
#         else    :
#             return False 
#     return True if length == 0 else False 
def solution(p):
    ansewr = '' 
    if len(p) == 0 or isCorrect(p) :
        return p;
    a,b = split(p) 
    print(a,b)
    
    if isCorrect(a) : # 올바름
        answer +=(a+solution(b))
    else : # 올바르지 않은 문자열 
        answer += ( '('+solution(b)+')') 
        for x in  a[1:-1] : 
            if x == '(' :
                answer += ')'
            else :
                answer += '('
    return answer 

solution("(()())()")
        
        
    
    
    
    
    