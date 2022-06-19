def solution(n, arr1, arr2):
    answer = []
    for x in [ list(bin(a|b)[2:])  for a,b in zip(arr1,arr2)] :
        answer.append(''.join([  "#" if q == '1' else " "   for q in ["0"] * ( n-len(x) )  + x   ] ))
    return answer
