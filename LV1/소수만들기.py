import math
temp = {} 
def check(num) :
    if temp.get(num) :
        return True 
    for i in range(2,int(math.sqrt(num))+1):
        if  num% i == 0 :
            return False
    temp[num] =True 
    return temp[num]

def solution(nums):
    answer = 0
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(i+1,nums_len):
            for k in range(j+1,nums_len) :
                if check(nums[i]+nums[j]+nums[k]):
                    answer +=1
                
    return answer