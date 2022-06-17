def solution(arr):
    arr.sort()
    answer = arr[0]
    for num in arr:
        if num%answer  == 0:
            answer = num
        elif num%answer !=0:
            i=j= 1
            while answer*i != num*j:
                if answer*i > num*j:
                    j+=1
                elif answer*i < num* j:
                    i +=1
            answer *= i
    return answer
