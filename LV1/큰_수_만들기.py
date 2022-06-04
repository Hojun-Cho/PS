def solution(number, k):
    # k개의 숫자를 제외하자 
    answer =[]
    ### 321 2 오름차순이면 다 들어간다 
    x= k 
    for num in number :
        while x > 0 and answer and  answer[-1] < num :
            answer.pop()
            x-=1 
        answer.append(num)
    return ''.join(answer[:len(number)-k])
