import math
def solution(left, right):
    answer = 0 
    for num in range(left ,right+1):
        answer -= num if math.sqrt(num).is_integer() else -num
    return answer
