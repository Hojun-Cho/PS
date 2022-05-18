from itertools import permutations
def solution(n):
    if n == 1 :return 1 
    if n == 2 : return 2 
    a,b= 1,2
    for i in range(3,n+1) : 
        result = a+b # 1,2      2 3 
        a,b = b,result  # 2 ,3   3 5
    return result %1234567