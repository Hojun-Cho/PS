from itertools import product
def solution(word):
    stack = []
    for i in range(1,6):
        # 중복 순열 
        for j in product(['A','E','I','O','U'],repeat =i):
            stack.append(''.join(j))
            
    stack.sort();
    return stack.index(word)+1