# 나의 풀이 
# def solution(N, stages):
#     #실패율 : 스테이지에 도달했으나 아직 클리어 못한 수 / 스테이지 도달 수 
#     #         n과 같음 /n보다 크거나 같음 
#     stages.sort()
#     max_stage = stages[-1]
#     rich = [0] *(N+2)
#     not_yet = [0] *(N+2)
#     answer =[]
    
#     for i in range(len(stages)):
#         not_yet[stages[i]] += 1
#         for j in range(1,stages[i]+1) :
#             rich[j] +=1 
    
#     for i in range(1,N+1) :
#         if rich[i] !=0:
#             answer.append([not_yet[i]/rich[i] ,i])
#         else :
#             answer.append([0 ,i])

#     answer.sort(reverse = True , key= lambda x :x[0])
#     result = [] 
#     for i in range(len(answer)) : 
#         result.append(answer[i][1])
#     return result

# 더 좋은 풀이 


def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        # 밑의 스테이지 사람을 제외하면 현재스테이지를 통과+도전중인 사람을 알 수 있다.
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    # value 값을 기준으로 정렬 
    return sorted(result, key=lambda x : result[x], reverse=True)

