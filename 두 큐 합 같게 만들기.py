def solution(queue1, queue2):
    answer = 0 
    s_1 ,s_2 = sum(queue1) ,sum(queue2)
    q = queue1 + queue2 
    target = (s_1+ s_2) //2 
    left , right = 0,len(queue1)
    limit = right * 3
    # 배열의 길이를 초과하는 경우 
    end = right * 2 
    for i in range(limit):
        if right  >= end or left >= end :
            return -1 
        if s_1 == target :
            return i 
        elif s_1 > target :
            s_1 -= q[left]
            s_2 += q[left]
            left +=1 
        else :
            s_1 += q[right]
            s_2 -= q[right]
            right +=1 
    return -1 
    
