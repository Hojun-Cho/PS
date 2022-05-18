def make_char(blank,x):
    x= x.upper() if blank else x.lower()
    return x 
def solution(s):
    answer = []
    blank = True 
    for x in list(s):
        if x.isalnum():
            answer.append(make_char(blank,x))
            blank = False
        else :
            blank = True 
            answer.append(x)
            
                
    return ''.join(answer)