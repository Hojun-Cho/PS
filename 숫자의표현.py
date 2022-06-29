def solution(n):
    answer = 0 
    for i in range(1,n):
        now = i 
        for j in range(i+1,n):
            if now + j > n :
                break
            if now + j == n :
                answer +=1
                break
            now += j
    return answer+1
