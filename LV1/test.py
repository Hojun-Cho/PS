from itertools import product
def solution(word):
    pattern = ['A','E','I','O','U']
    answer = 1
    stack = []
    for i in range(1,6):
        for j in product(pattern,repeat =i):
            stack.append(''.join(j))
            
    stack.sort();
    return stack.index(word)+1 
    
        
solution("AAAE");