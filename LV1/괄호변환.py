def isbalanced(s) : # 균형인지 확인한다.
    chk = 0
    for c in s :
        if c=='(' : 
            chk+=1 
        else :
            chk -=1 
    if chk == 0 :
        return True 
    return False 

def iscorrect(p):
    stack = []
    _len = 0 
    for c in p:
        if c == '(':
            stack.append(c)
            _len +=1 
        else:
            if  _len == 0:
                return False
            elif stack[-1] == '(':
                stack.pop()
                _len -= 1
    return False if _len >0  else True
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
    # u 는 올바른 문자열이 아니라면 
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
