def solution(n):
    a=b =1
    for i in range(2,n):
        a,b = b,a+b
    return b%1234567
