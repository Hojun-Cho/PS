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
