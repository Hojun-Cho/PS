def solution(nums):
    nums_len = 0
    key_len=0
    dic = {}
    for num in nums :
        nums_len +=1 
        if not dic.get(num) :
            dic[num]=1
            key_len +=1 

        else :
            dic[num] +=1 
            
    dic2 = sorted(dic.items(),key=lambda x:x)
    
    i=0
    answer =0 
    for x,y in dic2:
        if key_len > i and answer <nums_len//2 : 
            i+=1 
            answer +=1 
        
        
    
    return answer

def solution(nums):
    choose =  len(nums)// 2 
    nums = set(nums) 

    return min(choose,len(nums))
