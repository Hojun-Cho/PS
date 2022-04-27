def solution(N, stages):
    #실패율 : 스테이지에 도달했으나 아직 클리어 못한 수 / 스테이지 도달 수 
    #         n과 같음 /n보다 크거나 같음 
    stages.sort()
    max_stage = stages[-1]
    stages_len = N+1 
    rich = [0] *(N+2)
    not_yet = [0] *(N+2)
    answer =[]
    
    for i in range(len(stages)):
        not_yet[stages[i]] += 1
        for j in range(1,stages[i]+1) :
            rich[j] +=1 
    
    for i in range(1,N+1) :
        if rich[i] !=0:
            answer.append([not_yet[i]/rich[i] ,i])
        else :
            answer.append([0 ,i])

    answer.sort(reverse = True , key= lambda x :x[0])
    result = [] 
    for i in range(len(answer)) : 
        result.append(answer[i][1])
    return result

solution(3,[1,2,2,2,2,3,4,5,1,4,2,6,2])