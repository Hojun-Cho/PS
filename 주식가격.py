def solution(prices):
    stack  = [0]
    length = len(prices)
    answer = [0 for _ in range(length)]
    
    for i,price in enumerate(prices):
        while stack and  prices[stack[-1]] > price :
                j = stack.pop()      
                answer[j] = i-j
        stack.append(i)
    while stack :
        i= stack.pop()
        answer[i]= length - 1 - i 
    return answer
