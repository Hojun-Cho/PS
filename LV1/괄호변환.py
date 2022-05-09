def isbalanced(s) :
    chk = 0
    for c in s :
        if c=='(' : 
            chk+=1 
        else :
            chk -=1 
    if chk == 0 :
        return True 
    return False 
def iscorrect(s):
	stack=[]
	stack.append(s[0])
	for i in range(1,len(s)):
		if len(stack)==0 or stack[-1]==')' or (stack[-1]=='(' and s[i]=='('):
			stack.append(s[i])
		else:
			stack.pop()
	if len(stack)==0: return True
	else: return False


def solution(p) :
    answer = '' 
    u= ""
    v= "" 
    if len(p) ==  0 or iscorrect(p):
        return p 
    for i in range(2,len(p)+1,2) :
        if isbalanced(p[0:i]) :
            u = p[0:i] 
            v = p[i:len(p)]
            break 
    # u 는 균형잡힌 문자열
    if iscorrect(u) :
        answer += u+ solution(v) 
    else :
        answer += '(' + solution(v) +')'
        for x in u[1:-1]:
            if x == ')':
                answer += '('
            else :
                answer += ')'
    return answer 
<<<<<<< HEAD

    #################################################
def isbalanced(s) :
    chk = 0
    for c in s :
        if c=='(' : 
            chk+=1 
        else :
            chk -=1 
    if chk == 0 :
        return True 
    return False 
def iscorrect(s):
	stack = [] 
    for c in s :
        if c == '(':
            stack.append(c)
        else :
            if l == 0 :
                return False 
            elif stack[-1] == ')':
                stack.pop()
                l -=1 
    return True if l == 0 else False 


def solution(p) :
    answer = '' 
    u= ""
    v= "" 
    if len(p) ==  0 or iscorrect(p):
        return p 
    for i in range(2,len(p)+1,2) :
        if isbalanced(p[0:i]) :
            u = p[0:i] 
            v = p[i:len(p)]
            break 
    # u 는 균형잡힌 문자열
    if iscorrect(u) :
        answer += u+ solution(v) 
    else :
        answer += '(' + solution(v) +')'
        for x in u[1:-1]:
            if x == ')':
                answer += '('
            else :
                answer += ')'
    return answer 
=======
>>>>>>> 768af0be5cf2ad195bec88e38faab60ae66a565a
