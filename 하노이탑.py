def solution(n):
    answer = []
    def sol(n,start,mid,end) :
        if n == 1 :
            return answer.append([start,end])
        sol(n-1,start,end,mid)
        answer.append([start,end])
        sol(n-1,mid,start,end)
    sol(n,1,2,3)
    return answer
        
