def check(answer,arr):
    answer_index=0
    arr_index=0
    result = 0 
    while True :
        if answer_index >= len(answer) :
            return result 
        if arr_index >= len(arr) :
            arr_index = 0 
        if answer[answer_index] == arr[arr_index] :
            result+=1 
        arr_index +=1 
        answer_index +=1 
    return result 
            
    
        

def solution(answers):
    one=[1,2,3,4,5]
    two=[2, 1, 2, 3, 2, 4, 2, 5]
    three=[ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer =[]
    temp=[]
    
    
    temp.append(check(answers,one))
    temp.append(check(answers,two))
    temp.append(check(answers,three))
    
    _max= max(temp)
    
    for i in range(3):
        if _max == temp[i] :
            answer.append(i+1)
            
    return sorted(answer)

            

def solution(answers):
    one=[1,2,3,4,5]
    two=[2, 1, 2, 3, 2, 4, 2, 5]
    three=[3,3,1,1,2,2,4,4,5,5]
    answer =[]
    scores=[0,0,0]
    
    # 나누기를 하면 무한히 반복 가능하다 
    for i,num in enumerate(answers): 
        print(i,num)
        if num == one[i%len(one)]:
            scores[0] +=1 
        if num == two[i%len(two)] :
            scores[1] +=1 
        if num == three[i%len(three)]:
            scores[2] +=1 

    _max = max(scores)
    for i in range(3):
        if scores[i] == _max :
            answer.append(i+1) 

    return answer 