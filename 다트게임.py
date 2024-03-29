import re 
def solution(dartResult):
    arr = re.split(r"(\d+[SDT#*]{1,2})",dartResult)
    arr= [re.split(r"(\d+)",x)for x in arr]
    arr = [x[1:] if len(x[2]) ==1 else [x[1]]+ list(x[2])   for x in arr if len(x) != 1  ]
    answer = [0]
    dic = {'S':1,'D':2,'T':3 }
    for x in arr : 
        point = pow(int(x[0]),dic[x[1]]) 
        answer.append(point)
        if len(x)==3 :
            if x[2] == '#' :
                answer[-1] *=-1
            elif answer:
                answer[-1] *=2
                answer[-2] *=2
        
    return sum(answer)


def solution(dartResult: str)-> int:
    bounsMap = { "T" : 3 , "D" : 2 ,"S" : 1}
    nums = [0] 
    for s in dartResult:
        if bounsMap.get(s) != None :
            nums.append(nums[-1]**bounsMap[s])
            nums.append(0)
        elif s == "*" :
            nums[-2] *=2 
            if len(nums) >2 :
                nums[-3] *= 2
        elif s == "#":
            nums[-2] *= -1
        else :
            nums[-1] = nums[-1] * 10 + int(s)

    return sum(nums)
