def solution(n, lost, reserve):
    answer = 0
    arr = [1] * (n + 1)
    arr[0] = 0 

    for i,num in enumerate(reserve):
        arr[num] += 1

    for i,num in enumerate(lost):
        arr[num] -=1 
    
    for i in range(1,n) :
        if arr[i] >= 1 :
            answer +=1 

        elif arr[i] == 0 :
            if arr[i-1] == 2 :
                arr[i-1] = arr[i]=1
                answer +=1 
            elif arr[i+1] == 2   :
                arr[i+1] = arr[i]=  1 
                answer +=1 


    if arr[n] >= 1 or arr[n-1] == 2 :
        answer +=1 



    return answer