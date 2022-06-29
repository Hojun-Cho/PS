def solution(price, money, count):
    result = sum([price*N for N in range(1,count+1)]) - money
    return result if result > 0 else 0
