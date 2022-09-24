def solution(prices):
    length = len(prices)
    answer = [0] * length 
    for i in range(length-1):
        for j in range(i+1,length):
            if prices[i] > prices[j] :
                answer[i] +=1
                break 
            else :
                answer[i] +=1
    return answer 
    
