def solution(n):
    num= n+1
    binN = bin(n)[2: ]
    if (n&(n-1))==0 :
        return pow(n,2)
    if len(set(binN)) == 1 :
        return int('10' +''.join(binN[1:])   ,2)
    count_1  = binN.count('1')
    while (bin(num)[2:]).count('1') !=  count_1 :
        num+=1 
    return num
