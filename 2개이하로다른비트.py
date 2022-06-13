# 어려워...
def solution(numbers):
    answer = []
    for number in numbers :
        if number %2 == 0:
            answer.append(number+1)
        else :
            n =  '0'+bin(number)[2:]
            arr = list(n)
            idx =n.rfind('0')
            arr[idx] = '1' 
            arr[idx+1] = '0' 
            answer.append(int(''.join(arr),2))
    return answer
# 0101 
# 0111
# 0110

############

#  111
# 0111
# 1111
# 1011
