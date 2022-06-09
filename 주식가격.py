### 3 -> 2 -> 1 인경우
### i = 0 에서 stack.append( 0 ) 
### i = 1 에서 stack.pop()이 발생  j = 0  따라서 answer[j] = i-j  따라서 answer[0] = 1 그리고 stack.append(1) 
### i = 2 에서 stack.pop()이 발생  j = 1   따라서 answer[j] =i-j 따라서 answer[1]= 1그리고 stack.append(2)
### 마지막으로 stack.pop () 에서 j = 2가 되고 answer[2] = 3 - 2 - 1 = 0 으로 
## 답은 1,1,0가 된다 
### 이 시간은 현재 시간에서 남은 시간들 까지 주식의 값이 같거나 큰 경우의 시간들 ( 단 1초에서 2초로 가는 경우 1초동안 가격 3이 유지,2초에서 감소
### 즉 1초동안 유지

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

### 깔끔하게 풀어보기 ### 
def solution(prices):
    stack  = []
    length = len(prices)
    answer = [0 for _ in range(length)]
    
    def runIfBiggerThenNowIndex(i,price):
        while stack and prices[stack[-1]] > price:
            j= stack.pop()
            answer[j]=i-j
        stack.append(i)
    def setAnswer(i):
        answer[i] = length-1-i
        
    [ runIfBiggerThenNowIndex(i,price)  for i,price in enumerate(prices)]
    [ setAnswer(i) for i in stack ]
    return answer
