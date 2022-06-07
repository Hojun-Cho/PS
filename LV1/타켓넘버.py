answer = []
length = 0
def dfs(numbers,now_len,now_sum,now_arr,target,visit,now_index):
    global answer, length
    if   now_len == length and now_sum == target : 
        answer.append( now_arr)
        return 
    for i in range(now_index,length) :
        n= numbers[i]
        if not visit[i] :
            visit[i] = True 
            dfs(numbers,now_len+1,now_sum+n,now_arr+'+'+str(n),target,visit,i)
            visit[i]=False 
            visit[i] = True 
            dfs(numbers,now_len+1,now_sum-n,now_arr+'-'+str(n) ,target,visit,i)
            visit[i]=False 
              
def solution(numbers, target):
    global length 
    length = len(numbers)
    stack = [] 
    for i,n in enumerate(numbers):
        dfs(numbers,0,0,'',target,[False for _ in range(length)],i)
    return len(set(answer))
### 위의 풀이는 시간 초과 ### 
answer = 0
length = 0
numbers = []
target= 0
def dfs(now_sum,now_index,now_len):
    global length ,numbers,target,answer
    if  now_len == length and now_sum == target  :
        answer +=1 
        return
    if now_index > length-1 :
        return 
    dfs(now_sum+numbers[now_index],now_index+1,now_len+1)
    dfs(now_sum-numbers[now_index] ,now_index+1,now_len+1)
    
def solution(_input, _target):
    global length ,numbers,target,answer
    target = _target
    numbers = _input;
    length = len(numbers)
    dfs(0,0,0)
    return answer
